from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from .models import Question, Choice


class MyBarChartDrawing(Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self.add(HorizontalBarChart(), name='chart')

        question = q

        self.add(String(200, 180, "Question Title"), name='title')  # replace 'QUESTION' with question title

        # set any shapes, fonts, colors you want here.  We'll just
        # set a title font and place the chart within the drawing
        self.chart.x = 20
        self.chart.y = 20
        self.chart.width = self.width - 50
        self.chart.height = self.height - 40

        self.title.fontName = 'Helvetica-Bold'
        self.title.fontSize = 12

        votes = []
        for choice in question.choice_set.all:  # iterate through all the votes for a set question
            votes.append(choice.votes)  # add the number of votes for each question to the data

        self.chart.data = [votes]  # put data in chart


if __name__ == '__main__':
    # use the standard 'save' method to save barchart.gif, barchart.pdf etc
    # for quick feedback while working.
    MyBarChartDrawing().save(formats=['gif', 'png', 'jpg', 'pdf'], outDir='.', fnRoot='barchart')