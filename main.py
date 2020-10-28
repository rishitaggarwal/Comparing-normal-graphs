import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("height-weight.csv")
heightlist = df["Height(Inches)"].to_list()
weightlist = df["Weight(Pounds)"].to_list()
heightmean = statistics.mean(heightlist)
weightmean = statistics.mean(weightlist)
heightmode = statistics.mode(heightlist)
weightmode = statistics.mode(weightlist)
heightmedian = statistics.median(heightlist)
weightmedian = statistics.median(weightlist)
print("mean,median,mode of height is: {} ,{} ,{} respectively".format(heightmean,heightmedian,heightmode) )
print("mean,median,mode of weight is: {} ,{} ,{} respectively".format(weightmean,weightmedian,weightmode)  )

fig = ff.create_distplot([heightlist],["result"],show_hist = False)
fig1 = ff.create_distplot([weightlist],["result"],show_hist = False)

fig.show()
fig1.show()

stdht = statistics.stdev(heightlist)
stdwt = statistics.stdev(weightlist)

print("the standard deviation of height and weight is: {},{} respectively".format(stdht,stdwt))
height1ststart,height1stend = heightmean - stdht,heightmean + stdht
height2ststart,height2stend = heightmean - (2*stdht),heightmean + (2*stdht)
height3ststart,height3stend = heightmean - (3*stdht),heightmean + (3*stdht)

weight1ststart,weight1stend = weightmean - stdwt,weightmean + stdwt
weight2ststart,weight2stend = weightmean - (2*stdwt),weightmean + (2*stdwt)
weight3ststart,weight3stend = weightmean - (3*stdwt),weightmean + (3*stdwt)

height1std = [result for result in heightlist if result > height1ststart and result < height1stend]
height2std = [result for result in heightlist if result > height2ststart and result < height2stend]
height3std = [result for result in heightlist if result > height3ststart and result < height3stend]

weight1std = [result for result in weightlist if result > weight1ststart and result < weight1stend]
weight2std = [result for result in weightlist if result > weight2ststart and result < weight2stend]
weight3std = [result for result in weightlist if result > weight3ststart and result < weight3stend]

print("{}% of data for height lies within 1st std".format(len(height1std)*100/len(heightlist)))
print("{}% of data for weight lies within 1st std".format(len(weight1std)*100/len(weightlist)))
print("{}% of data for height lies within 2st std".format(len(height2std)*100/len(heightlist)))
print("{}% of data for weight lies within 2st std".format(len(weight2std)*100/len(weightlist)))
print("{}% of data for height lies within 3st std".format(len(height3std)*100/len(heightlist)))
print("{}% of data for weight lies within 3st std".format(len(weight3std)*100/len(weightlist)))