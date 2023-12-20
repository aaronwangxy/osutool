from django.shortcuts import render, get_object_or_404
from .forms import PlayerName
from .models import Player, Score, Insights, Suggested
from ossapi import Ossapi
from collections import defaultdict

client_id = -1
client_secret = ""
api = Ossapi(client_id, client_secret)

# Create your views here.
def info(request, playername):
    userid = api.user(playername).id
    player, created = Player.objects.get_or_create(name=playername, player_id=userid)
    
    scores = api.user_scores(user_id=userid, type="best", limit=100)
    for score in scores:
        Score.objects.get_or_create(
            player = player, 
            title = score.beatmapset.title,
            beatmap_link = score.beatmap.url,
            pp = score.pp,
            accuracy = score.accuracy,
            mods = score.mods,
            rank = score.rank,
            star_rating = score.beatmap.difficulty_rating,
            length = score.beatmap.total_length,
        )

    queryset = Score.objects.filter(player=player)
    insight_scores = []
    for query in queryset:
        insight_scores.append(query)
    insight_scores.sort(reverse=True, key=lambda x: x.pp)
    avg_acc = 0
    avg_len = 0
    mod_freq = defaultdict(int)
    for i in range(10):
        avg_acc += insight_scores[i].accuracy / 10
        avg_len += insight_scores[i].length / 10
        mod_freq[insight_scores[i].mods] += 1
    fav_mod = max(mod_freq, key=mod_freq.get)

    insights, created = Insights.objects.get_or_create(
        player = player,
        avg_accuracy = avg_acc,
        avg_map_length = avg_len,
        fav_mod = fav_mod,
        farmable_pp = insight_scores[9].pp
    )

    context = {
        'username' : playername,
        'userid' : userid,
        'scores' : scores,
        'insights' : insights
    }
    return render(request, 'player/player.html', context)


def player(request):
    if request.method == "POST":
        form = PlayerName(request.POST)
        if form.is_valid():
            return info(request, form.cleaned_data['playername'])
    else:
        form = PlayerName()
    context = {'form' : form}
    return render(request, 'player/base.html', context)