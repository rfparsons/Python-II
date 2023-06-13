from django.shortcuts import render
from django.http import HttpResponse

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure

# Create your views here.
def graph2(request):
    plot1 = figure()
    x1=[1, 2, 3, 4, 5]
    y1=[2, 4, 3, 3.5, 6]
    plot1.line(x1, y1)
    

    script, div = components(plot1, CDN)

    return render(request, "index_graph.html", {"the_script": script, "the_div": div})

def graph(request):
    plot2 = figure()
    values = [15, 25, 50, 10]
    colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
    plot2.vbar(x=range(len(values)), top=values, width=0.5, color=colors)
    

    script, div = components(plot2, CDN)

    return render(request, "index_graph.html", {"the_script": script, "the_div": div})