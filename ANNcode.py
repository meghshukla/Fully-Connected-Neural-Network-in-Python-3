import math
import numpy
#REMOVE del OutputData
exp=math.e

#600:  I/P: [1,600,125,20],[1,600,125,24],[1,600,125,28],[1,600,125,32],[1,600,125,36],[1,600,125,40],[1,600,125,44],[1,600,125,47]
#800:  I/P: [1,800,93.75,15],[1,800,93.7499,18.75],[1,800,93.7499,18.75],[1,800,93.75,22.5],[1,800,93.75,26.25],[1,800,93.75,30],[1,800,93.75,33.75],[1,800,93.75,37.5]
#1000: I/P: [1,1000,75,12],[1,1000,75,15],[1,1000,75,18],[1,1000,75,21],[1,1000,75,24],[1,1000,75,27],[1,1000,75,30]
#1400: I/P: [1,1400,53.5715,9],[1,1400,53.5715,11],[1,1400,53.5715,13],[1,1400,53.5715,15],[1,1400,53.5715,17],[1,1400,53.5715,19],[1,1400,53.5715,21]
#1800: I/P: [1,1800,41.666,7],[1,1800,41.666,8.5],[1,1800,41.666,10],[1,1800,41.666,11.5],[1,1800,41.666,13],[1,1800,41.666,14.5],[1,1800,41.666,16]
#2200: I/P: [1,2200,34.0909,5.5],[1,2200,34.0909,6.5],[1,2200,34.0909,7.5],[1,2200,34.0909,8.5],[1,2200,34.0909,9.5],[1,2200,34.0909,10.5],[1,2200,34.0909,11.5],[1,2200,34.0909,12.5],[1,2200,34.0909,13.5]
#2600: I/P: [1,2600,28.8462,5],[1,2600,28.8462,5.5],[1,2600,28.8462,7],[1,2600,28.8462,8.5],[1,2600,28.8462,9],[1,2600,28.8462,10],[1,2600,28.8462,11.5]
#3000: I/P: [1,3000,25,4],[1,3000,25,4.8],[1,3000,25,5.5],[1,3000,25,6.7],[1,3000,25,7],[1,3000,25,8.5],[1,3000,25,9.4],[1,3000,25,10]
#3400: I/P: [1,3400,22.0588,4],[1,3400,22.0588,4.5],[1,3400,22.0588,5],[1,3400,22.0588,5.5],[1,3400,22.0588,6],[1,3400,22.0588,6.5],[1,3400,22.0588,7],[1,3400,22.0588,7.5],[1,3400,22.0588,8],[1,3400,22.0588,8.5]
#3800: I/P: [1,3800,19.736,4],[1,3800,19.736,4.5],[1,3800,19.736,5],[1,3800,19.736,5.5],[1,3800,19.736,6],[1,3800,19.736,6.5],[1,3800,19.736,7]
#4200: I/P: [1,4200,17.8571,2.8],[1,4200,17.8571,3.5],[1,4200,17.8571,4.2],[1,4200,17.8571,4.9],[1,4200,17.8571,5.6],[1,4200,17.8571,6.3],[1,4200,17.8571,7.1]
#4600: I/P: [1,4600,16.3043,3],[1,4600,16.3043,3.5],[1,4600,16.3043,4],[1,4600,16.3043,4.5],[1,4600,16.3043,5],[1,4600,16.3043,5.5],[1,4600,16.3043,6],[1,4600,16.3043,6.5]
#5000: I/P: [1,5000,15,2.5],[1,5000,15,3],[1,5000,15,3.5],[1,5000,15,4],[1,5000,15,4.5],[1,5000,15,5],[1,5000,15,5.5],[1,5000,15,6]
#5400: I/P: [1,5400,13.8888,2.2],[1,5400,13.8888,2.7],[1,5400,13.8888,3.2],[1,5400,13.8888,3.7],[1,5400,13.8888,4.2],[1,5400,13.8888,4.7],[1,5400,13.8888,5.2]
#5600: I/P: [1,5600,13.39286,2.2],[1,5600,13.39286,2.4],[1,5600,13.39286,2.8]
#5800: I/P: [1,5800,12.9310,2.3],[1,5800,12.9310,2.6],[1,5800,12.9310,2.9],[1,5800,12.9310,3.2],[1,5800,12.9310,3.5],[1,5800,12.9310,3.8],[1,5800,12.9310,4.1],[1,5800,12.9310,4.4],[1,5800,12.9310,4.7],[1,5800,12.9310,5.0]
#6000: I/P: [1,6000,12.5,2],[1,6000,12.5,2.5],[1,600,12.5,3],[1,6000,12.5,3.5],[1,6000,12.5,4],[1,6000,12.5,4.5],[1,6000,12.5,5]
#6200: I/P: [1,6200,12.09677,2],[1,6200,12.09677,2.4],[1,6200,12.09677,2.8],[1,6200,12.09677,3.2],[1,6200,12.09677,3.6],[1,6200,12.09677,4],[1,6200,12.09677,4.4],[1,6200,12.09677,4.8]

#600:  O/P: [124.8,0.005],[123,0.0833],[120.3,0.16786],[117.8,0.225],[115.1,0.275],[113.2,0.295],[110.7,0.325],[108.1,0.359]
#800:  O/P: [93.65,0.006667],[91,0.146667],[88.9,0.2152222],[86.8,0.2647142],[84.6,0.305],[82.4,0.33629],[80.4,0.356]
#1000: O/P: [74.9,0.00833],[72.9,0.14],[70.9,0.2277],[68.5,0.3095],[66.8,0.341666],[64.9,0.37407],[63,0.4]
#1400: O/P: [53,0.0635],[51.4,0.19741],[50,0.27473],[48.7,0.324767],[47.5,0.357147],[46,0.3985],[44.8,0.41769]
#1800: O/P: [41.6,0.009],[39.8,0.21953],[38.8,0.28666],[37.7,0.34492],[36.7,0.382046],[35.8,0.40459],[34.5,0.44791]
#2200: O/P: [33.4,0.1256],[32.5,0.2447],[31.7,0.3187],[30.9,0.3754],[30.1,0.42],[29.3,0.4563],[28.6,0.4775],[27.9,0.495272],[27.1,0.5178]
#2600: O/P: [29.12,0.12424],[27.6,0.22658],[26.4,0.34946],[25.4,0.4054],[25,0.42736],[24.25,0.45962],[23,0.5084]
#3000: O/P: [24.7,0.075],[24.04,0.2],[23.2,0.32727],[22.35,0.39552],[22.1,0.4143],[20.8,0.494117],[20.16,0.51489],[19.6,0.54]
#3400: O/P: [21.1,0.2397],[20.65,0.3131],[20.2,0.37176],[19.7,0.42887],[19.3,0.4598],[18.9,0.4860],[18.5,0.5084],[18.05,0.5345],[17.6,0.5573],[17.2,0.57162]
#3800: O/P: [18.45,0.3215],[18.05,0.37467],[17.62,0.4232],[17.25,0.452],[16.88,0.476],[16.5,0.4978],[16.14,0.5137]
#4200: O/P: [17.6,0.09182],[16.75,0.3163],[16.15,0.40645],[15.58,0.46471],[15.02,0.5066],[14.33,0.557],[13.74,0.57987]
#4600: O/P: [15.45,0.2847],[15,0.3726],[14.6,0.426075],[14.16,0.4765],[13.75,0.51086],[13.25,0.5553],[12.8,0.58405],[12.4,0.6006]
#5000: O/P: [14.65,0.14],[14,0.33333],[13.55,0.4143],[13.15,0.4625],[12.72,0.506667],[12.32,0.536],[11.92,0.56],[11.4,0.6]
#5400: O/P: [13.67,0.1],[13.18,0.26255],[12.56,0.415275],[12.15,0.47],[11.69,0.5235],[11.29,0.5529],[10.785,0.5969]
#5600: O/P: [13.1,0.133118],[12.9,0.2054],[12.36,0.36888]
#5800: O/P: [12.5,0.18739],[12.2,0.2811],[11.75,0.4072],[11.5,0.44718],[11.25,0.4803],[11,0.5081],[10.7,0.53414],[10.48,0.55704],[10.25,0.57043],[10,0.5862]
#6000: O/P: [12.3,0.0333333],[11.8,0.28],[11.2,0.4333333],[10.76,0.49714],[10.32,0.545],[9.9,0.577777],[9.42,0.616]
#6200: O/P: [11.84,0.128385],[11.44,0.27365],[10.94,0.41313],[10.56,0.4802],[10.2,0.52688],[9.88,0.5542],[9.57,0.5742],[9.28,0.58683]

#One 5600 h added

inputData=[[1,600,125,20],[1,600,125,24],[1,600,125,28],[1,600,125,32],[1,600,125,36],[1,600,125,40],[1,600,125,44],[1,600,125,47],[1,800,93.75,15],[1,800,93.75,18.75],[1,800,93.75,18.7500001],[1,800,93.75,22.5],[1,800,93.75,26.25],[1,800,93.75,30],[1,800,93.75,33.75],[1,800,93.75,37.5],[1,1000,75,12],[1,1000,75,15],[1,1000,75,18],[1,1000,75,21],[1,1000,75,24],[1,1000,75,27],[1,1000,75,30],[1,1400,53.5715,9],[1,1400,53.5715,11],[1,1400,53.5715,13],[1,1400,53.5715,15],[1,1400,53.5715,17],[1,1400,53.5715,19],[1,1400,53.5715,21],[1,1800,41.666,7],[1,1800,41.666,8.5],[1,1800,41.666,10],[1,1800,41.666,11.5],[1,1800,41.666,13],[1,1800,41.666,14.5],[1,1800,41.666,16],[1,2200,34.0909,5.5],[1,2200,34.0909,6.5],[1,2200,34.0909,7.5],[1,2200,34.0909,8.5],[1,2200,34.0909,9.5],[1,2200,34.0909,10.5],[1,2200,34.0909,11.5],[1,2200,34.0909,12.5],[1,2200,34.0909,13.5],[1,2600,28.8462,5],[1,2600,28.8462,5.5],[1,2600,28.8462,7],[1,2600,28.8462,8.5],[1,2600,28.8462,9],[1,2600,28.8462,10],[1,2600,28.8462,11.5],[1,3000,25,4],[1,3000,25,4.8],[1,3000,25,5.5],[1,3000,25,6.7],[1,3000,25,7],[1,3000,25,8.5],[1,3000,25,9.4],[1,3000,25,10],[1,3400,22.0588,4],[1,3400,22.0588,4.5],[1,3400,22.0588,5],[1,3400,22.0588,5.5],[1,3400,22.0588,6],[1,3400,22.0588,6.5],[1,3400,22.0588,7],[1,3400,22.0588,7.5],[1,3400,22.0588,8],[1,3400,22.0588,8.5],[1,3800,19.736,4],[1,3800,19.736,4.5],[1,3800,19.736,5],[1,3800,19.736,5.5],[1,3800,19.736,6],[1,3800,19.736,6.5],[1,3800,19.736,7],[1,4200,17.8571,2.8],[1,4200,17.8571,3.5],[1,4200,17.8571,4.2],[1,4200,17.8571,4.9],[1,4200,17.8571,5.6],[1,4200,17.8571,6.3],[1,4200,17.8571,7.1],[1,4600,16.3043,3],[1,4600,16.3043,3.5],[1,4600,16.3043,4],[1,4600,16.3043,4.5],[1,4600,16.3043,5],[1,4600,16.3043,5.5],[1,4600,16.3043,6],[1,4600,16.3043,6.5],[1,5000,15,2.5],[1,5000,15,3],[1,5000,15,3.5],[1,5000,15,4],[1,5000,15,4.5],[1,5000,15,5],[1,5000,15,5.5],[1,5000,15,6],[1,5400,13.8888,2.2],[1,5400,13.8888,2.7],[1,5400,13.8888,3.2],[1,5400,13.8888,3.7],[1,5400,13.8888,4.2],[1,5400,13.8888,4.7],[1,5400,13.8888,5.2],[1,5600,13.39286,2.2],[1,5800,12.9310,2.3],[1,5800,12.9310,2.6],[1,5800,12.9310,2.9],[1,5800,12.9310,3.2],[1,5800,12.9310,3.5],[1,5800,12.9310,3.8],[1,5800,12.9310,4.1],[1,5800,12.9310,4.4],[1,5800,12.9310,4.7],[1,5800,12.9310,5.0],[1,6000,12.5,2],[1,6000,12.5,2.5],[1,6000,12.5,3],[1,6000,12.5,3.5],[1,6000,12.5,4],[1,6000,12.5,4.5],[1,6000,12.5,5],[1,6200,12.09677,2],[1,6200,12.09677,2.4],[1,6200,12.09677,2.8],[1,6200,12.09677,3.2],[1,6200,12.09677,3.6],[1,6200,12.09677,4],[1,6200,12.09677,4.4],[1,6200,12.09677,4.8],'i']
outputData=[[124.8,0.005],[123,0.0833],[120.3,0.16786],[117.8,0.225],[115.1,0.275],[113.2,0.295],[110.7,0.325],[108.1,0.359],[93.65,0.006667],[91,0.146666],[91,0.146667],[88.9,0.2152222],[86.8,0.2647142],[84.6,0.305],[82.4,0.33629],[80.4,0.356],[74.9,0.00833],[72.9,0.14],[70.9,0.2277],[68.5,0.3095],[66.8,0.341666],[64.9,0.37407],[63,0.4],[53,0.0635],[51.4,0.19741],[50,0.27473],[48.7,0.324767],[47.5,0.357147],[46,0.3985],[44.8,0.41769],[41.6,0.009],[39.8,0.21953],[38.8,0.28666],[37.7,0.34492],[36.7,0.382046],[35.8,0.40459],[34.5,0.44791],[33.4,0.1256],[32.5,0.2447],[31.7,0.3187],[30.9,0.3754],[30.1,0.42],[29.3,0.4563],[28.6,0.4775],[27.9,0.495272],[27.1,0.5178],[28.26,0.11723],[27.6,0.22658],[26.4,0.34946],[25.4,0.4054],[25,0.42736],[24.25,0.45962],[23,0.5084],[24.7,0.075],[24.04,0.2],[23.2,0.32727],[22.35,0.39552],[22.1,0.4143],[20.8,0.494117],[20.16,0.51489],[19.6,0.54],[21.1,0.2397],[20.65,0.3131],[20.2,0.37176],[19.7,0.42887],[19.3,0.4598],[18.9,0.4860],[18.5,0.5084],[18.05,0.5345],[17.6,0.5573],[17.2,0.57162],[18.45,0.3215],[18.05,0.37467],[17.62,0.4232],[17.25,0.452],[16.88,0.476],[16.5,0.4978],[16.14,0.5137],[17.6,0.09182],[16.75,0.3163],[16.15,0.40645],[15.58,0.46471],[15.02,0.5066],[14.33,0.557],[13.74,0.57987],[15.45,0.2847],[15,0.3726],[14.6,0.426075],[14.16,0.4765],[13.75,0.51086],[13.25,0.5553],[12.8,0.58405],[12.4,0.6006],[14.62,0.14],[14,0.33333],[13.55,0.4143],[13.15,0.4625],[12.72,0.506667],[12.32,0.536],[11.92,0.56],[11.4,0.6],[13.67,0.1],[13.18,0.26255],[12.56,0.415275],[12.08,0.4886],[11.69,0.5235],[11.29,0.5529],[10.785,0.5969],[13.1,0.133118],[12.5,0.18739],[12.2,0.2811],[11.75,0.4072],[11.5,0.44718],[11.25,0.4803],[11,0.5081],[10.7,0.53414],[10.48,0.55704],[10.25,0.57043],[10,0.5862],[12.3,0.0333333],[11.8,0.28],[11.2,0.4333333],[10.76,0.49714],[10.32,0.545],[9.9,0.577777],[9.42,0.616],[11.84,0.128385],[11.44,0.27365],[10.94,0.41313],[10.56,0.4802],[10.2,0.52688],[9.88,0.5542],[9.57,0.5742],[9.28,0.58683],'o']

#inputData=[[1,600,125,20],[1,600,125,24],[1,600,125,28],[1,600,125,32],[1,600,125,36],[1,600,125,40],[1,600,125,44],[1,600,125,47],[1,800,93.75,15],[1,800,93.75,18.75],[1,800,93.7499,18.75],[1,800,93.75,22.5],[1,800,93.75,26.25],[1,800,93.75,30],[1,800,93.75,33.75],[1,800,93.75,37.5],[1,1000,75,12],[1,1000,75,15],[1,1000,75,18],[1,1000,75,21],[1,1000,75,24],[1,1000,75,27],[1,1000,75,30],[1,1400,53.5715,9],[1,1400,53.5715,11],[1,1400,53.5715,13],[1,1400,53.5715,15],[1,1400,53.5715,17],[1,1400,53.5715,19],[1,1400,53.5715,21],[1,1800,41.666,7],[1,1800,41.666,8.5],[1,1800,41.666,10],[1,1800,41.666,11.5],[1,1800,41.666,13],[1,1800,41.666,14.5],[1,1800,41.666,16],[1,2200,34.0909,5.5],[1,2200,34.0909,6.5],[1,2200,34.0909,7.5],[1,2200,34.0909,8.5],[1,2200,34.0909,9.5],[1,2200,34.0909,10.5],[1,2200,34.0909,11.5],[1,2200,34.0909,12.5],[1,2200,34.0909,13.5],[1,2600,28.8462,5],[1,2600,28.8462,5.5],[1,2600,28.8462,7],[1,2600,28.8462,8.5],[1,2600,28.8462,9],[1,2600,28.8462,10],[1,2600,28.8462,11.5],[1,3000,25,4],[1,3000,25,4.8],[1,3000,25,5.5],[1,3000,25,6.7],[1,3000,25,7],[1,3000,25,8.5],[1,3000,25,9.4],[1,3000,25,10],[1,3400,22.0588,4],[1,3400,22.0588,4.5],[1,3400,22.0588,5],[1,3400,22.0588,5.5],[1,3400,22.0588,6],[1,3400,22.0588,6.5],[1,3400,22.0588,7],[1,3400,22.0588,7.5],[1,3400,22.0588,8],[1,3400,22.0588,8.5],[1,3800,19.736,4],[1,3800,19.736,4.5],[1,3800,19.736,5],[1,3800,19.736,5.5],[1,3800,19.736,6],[1,3800,19.736,6.5],[1,3800,19.736,7],[1,4200,17.8571,2.8],[1,4200,17.8571,3.5],[1,4200,17.8571,4.2],[1,4200,17.8571,4.9],[1,4200,17.8571,5.6],[1,4200,17.8571,6.3],[1,4200,17.8571,7.1],[1,4600,16.3043,3],[1,4600,16.3043,3.5],[1,4600,16.3043,4],[1,4600,16.3043,4.5],[1,4600,16.3043,5],[1,4600,16.3043,5.5],[1,4600,16.3043,6],[1,4600,16.3043,6.5],[1,5000,15,2.5],[1,5000,15,3],[1,5000,15,3.5],[1,5000,15,4],[1,5000,15,4.5],[1,5000,15,5],[1,5000,15,5.5],[1,5000,15,6],[1,5400,13.8888,2.2],[1,5400,13.8888,2.7],[1,5400,13.8888,3.2],[1,5400,13.8888,3.7],[1,5400,13.8888,4.2],[1,5400,13.8888,4.7],[1,5400,13.8888,5.2],[1,5600,13.39286,2.2],[1,5800,12.9310,2.3],[1,5800,12.9310,2.6],[1,5800,12.9310,2.9],[1,5800,12.9310,3.2],[1,5800,12.9310,3.5],[1,5800,12.9310,3.8],[1,5800,12.9310,4.1],[1,5800,12.9310,4.4],[1,5800,12.9310,4.7],[1,5800,12.9310,5.0],[1,6000,12.5,2],[1,6000,12.5,2.5],[1,6000,12.5,3],[1,6000,12.5,3.5],[1,6000,12.5,4],[1,6000,12.5,4.5],[1,6000,12.5,5],[1,6200,12.09677,2],[1,6200,12.09677,2.4],[1,6200,12.09677,2.8],[1,6200,12.09677,3.2],[1,6200,12.09677,3.6],[1,6200,12.09677,4],[1,6200,12.09677,4.4],[1,6200,12.09677,4.8],'i']
#outputData=[[124.8,0.005],[123,0.0833],[120.3,0.16786],[117.8,0.225],[115.1,0.275],[113.2,0.295],[110.7,0.325],[108.1,0.359],[93.65,0.006667],[91,0.146666],[91,0.146667],[88.9,0.2152222],[86.8,0.2647142],[84.6,0.305],[82.4,0.33629],[80.4,0.356],[74.9,0.00833],[72.9,0.14],[70.9,0.2277],[68.5,0.3095],[66.8,0.341666],[64.9,0.37407],[63,0.4],[53,0.0635],[51.4,0.19741],[50,0.27473],[48.7,0.324767],[47.5,0.357147],[46,0.3985],[44.8,0.41769],[41.6,0.009],[39.8,0.21953],[38.8,0.28666],[37.7,0.34492],[36.7,0.382046],[35.8,0.40459],[34.5,0.44791],[33.4,0.1256],[32.5,0.2447],[31.7,0.3187],[30.9,0.3754],[30.1,0.42],[29.3,0.4563],[28.6,0.4775],[27.9,0.495272],[27.1,0.5178],[29.12,0.12424],[27.6,0.22658],[26.4,0.34946],[25.4,0.4054],[25,0.42736],[24.25,0.45962],[23,0.5084],[24.7,0.075],[24.04,0.2],[23.2,0.32727],[22.35,0.39552],[22.1,0.4143],[20.8,0.494117],[20.16,0.51489],[19.6,0.54],[21.1,0.2397],[20.65,0.3131],[20.2,0.37176],[19.7,0.42887],[19.3,0.4598],[18.9,0.4860],[18.5,0.5084],[18.05,0.5345],[17.6,0.5573],[17.2,0.57162],[18.45,0.3215],[18.05,0.37467],[17.62,0.4232],[17.25,0.452],[16.88,0.476],[16.5,0.4978],[16.14,0.5137],[17.6,0.09182],[16.75,0.3163],[16.15,0.40645],[15.58,0.46471],[15.02,0.5066],[14.33,0.557],[13.74,0.57987],[15.45,0.2847],[15,0.3726],[14.6,0.426075],[14.16,0.4765],[13.75,0.51086],[13.25,0.5553],[12.8,0.58405],[12.4,0.6006],[14.62,0.14],[14,0.33333],[13.55,0.4143],[13.15,0.4625],[12.72,0.506667],[12.32,0.536],[11.92,0.56],[11.4,0.6],[13.67,0.1],[13.18,0.26255],[12.56,0.415275],[12.08,0.4886],[11.69,0.5235],[11.29,0.5529],[10.785,0.5969],[13.1,0.133118],[12.5,0.18739],[12.2,0.2811],[11.75,0.4072],[11.5,0.44718],[11.25,0.4803],[11,0.5081],[10.7,0.53414],[10.48,0.55704],[10.25,0.57043],[10,0.5862],[12.3,0.0333333],[11.8,0.28],[11.2,0.4333333],[10.76,0.49714],[10.32,0.545],[9.9,0.577777],[9.42,0.616],[11.84,0.128385],[11.44,0.27365],[10.94,0.41313],[10.56,0.4802],[10.2,0.52688],[9.88,0.5542],[9.57,0.5742],[9.28,0.58683],'o']

a=outputData[:]
for i in range(len(a)-1):
    del outputData[i][1]
#print outputData    

maxNormalOP=[]
maxNormalIP=[]

EpochMax=0
Error=[0]*11                                                                   #Change multiplier value according to Epoch count
error_index=0

ErrorFrequency=[0]*15

FinalWeight=[0,0,0]

def sigmoid(lamb,ip,threshold):
    '''
    Computes sigmoidal values for given sigmoidal gain lamb
    I/P=lambda,input,threshold[
    return sigmoid value
    '''
    result=[]
    for e in ip:
        result.append(1.0/(1+pow(exp,-lamb*(e-threshold))))  
    return result     
    
def inputLog(ip):
    '''
    Facilitates augmented BP by calculating logarithmic nodes
    I/P is value of normal neuron input
    return calculated log value
    ''' 
    return math.log(1.175*ip+1.543)
    
def inputExp(ip):  
    '''
    Facilitates augmented BP by calculating exponential nodes
    I/P is value of normal neuron input
    return calculated exponential value
    '''
    return 0.851*pow(exp,ip)-1.313
    
def outputLog(ip):
    '''
    Facilitates augmented BP by calculating logarithmic nodes
    I/P is value of normal neuron ouput
    return calculated log value
    ''' 
    return math.log(1.718*ip+1)
    
def outputExp(ip):  
    '''
    Facilitates augmented BP by calculating exponential nodes
    I/P is value of normal neuron output
    return calculated exponential value
    '''
    return pow(exp,0.6931*ip-1)
    
def Sort():
    '''
    arranges practical radius ie Output Data in ascending order
    arranges input data according to how output data arranged
    '''
    global inputData
    global outputData
    temp1=outputData[:]
    temp1.sort()
    temp2=[0]*len(temp1)
    for i in range(len(temp1)):
        j=outputData.index(temp1[i])
        temp2[i]=inputData[j]
    inputData=temp2[:]
    outputData=temp1[:]
    del temp1
    del temp2
    
def normalizeData(data):  
    global maxNormalOP
    global maxNormalIP
    for i in range(len(data[0])):
        maximum=data[0][i]
        for e in range(len(data)-1):
            if(data[e][i]>maximum):
                maximum=data[e][i]
        maximum=1.3*maximum        
        #print(data[e][i])        
        if(data[-1]=='o'):
            maxNormalOP.append(maximum)
        else:
            maxNormalIP.append(maximum)        
        for e in range(len(data)-1):
            data[e][i]/=float(maximum)                    
    return data
               
        
def augmentData(data):                                                          #the input data list is 
    '''                                                                         #manipulated permanently
    Inserts exponential and logarithmic input for respective neurons
    '''  
    for e in range(len(data)-1):
        copy=data[e][:]                                                         #since we're itering over data
        for i in range(len(copy)):                                             #changes to the data can't be made directly  
            if(data[-1]=='i'):
                data[e].insert(3*i+1,inputLog(copy[i]))
                data[e].insert(3*i+2,inputExp(copy[i]))
            else:
                data[e].insert(3*i+1,outputLog(copy[i]))
                data[e].insert(3*i+2,outputExp(copy[i]))    
    return data
    
    
             
class ANN():
    '''
    Defines ANN architecture such as number of i/p, hidden
    and o/p nodes. Creates random weights
    '''
    def __init__(self,arraySize,networkParameters,augbackprop):
        self.augbackprop=augbackprop                                            #usage of augmented backpropagation
        if self.augbackprop==1:                                                 #
            self.outputNodes=arraySize[-1]*3                                    #we need three output nodes for augmented backprop
            self.inputNodes=arraySize[0]*3                                      #
        else:                                                                   #
            self.inputNodes=arraySize[0]
            self.outputNodes=arraySize[-1]                                      #   
        if(len(arraySize)>=3):
            self.hiddenNodes=[0]*(len(arraySize)-2)                             #for multiple hidden nodes
            i=1
            for e in range(len(arraySize)-2):
                self.hiddenNodes[e]=arraySize[i]
                i+=1
        self.lamb=networkParameters[0]                                          #
        self.threshold=networkParameters[1]                                     #init network parameters
        self.learnRate=networkParameters[2]                                     #
        self.alpha=networkParameters[3]                                         #
        if(len(arraySize)>=3):
            self.flat_list=[self.inputNodes]+self.hiddenNodes+[self.outputNodes]
        else:
            self.flat_list=[self.inputNodes]+[self.outputNodes] 
        print(self.flat_list)       
        self.weights=[0]*(len(self.flat_list)-1)
        for i in range(len(self.flat_list)-1):                                                    #random weights initialized
             self.weights[i]=numpy.random.rand(self.flat_list[i],self.flat_list[i+1])
            
    def __str__(self):
        return 'ANN with input node :'+str(self.inputNodes)+'\nANN with output node :'+str(self.outputNodes)+'\nANN with hidden node s:'+str(self.hiddenNodes)
        

class Layers():
    '''
    Class is constructed to identify individual
    layers in the neural network.
    Defines input and output of the layer post activation function
    '''
    def __init__(self,layer_number,ann):                                        #ann is a global variable. to access variable we dont need
        self.layer_number=layer_number                                          #to use global. But if we modify it, we use global 
        self.ann=ann
        
    def input(self,inData):
        if(self.layer_number==0):       #receives  1xk, post: kx1               #if layer is 0, input is training data.                                            
            self.input=numpy.transpose(numpy.asmatrix(inData))                  #else input is output of previous layer
            '''
            print 'Sigmoid input of Layer : '+str(self.layer_number)
            print self.input
            print '\n'
            '''
        else:
            self.input=numpy.transpose(numpy.asmatrix(sigmoid(self.ann.lamb,numpy.array(inData).flatten().tolist(),self.ann.threshold)))      #np.array(m).flatten().tolist() --> to convert matrix to list
            '''
            print 'Sigmoid input of Layer : '+str(self.layer_number)
            print self.input
            print '\n'  
            ''' 
         
    def output(self):
        if(self.layer_number==len(self.ann.flat_list)-1):   #input kx1, post: 1xk
            self.output=numpy.array(numpy.transpose(numpy.asmatrix(self.input))).flatten().tolist()
            '''
            print 'Output of Final Layer : '+str(self.layer_number)
            print self.output
            print '\n'
            '''
        else:
            '''
            print 'Weight : '+str(self.layer_number)
            print numpy.asmatrix(numpy.transpose(self.ann.weights[self.layer_number]))
            print '\n'
            '''
            self.output=numpy.transpose(numpy.asmatrix(numpy.transpose(self.ann.weights[self.layer_number]))*numpy.asmatrix(self.input))    #to multiply matrices we need to declare the as matrix   
            '''
            print 'Output of layer : '+str(self.layer_number)
            print self.output
            print '\n' 
            '''
        
        
def script(): 
    x=eval(input('Enter number of neurons in input, hidden(s) and ouput layer\n'))  
    y=eval(input('Enter sigmoidal gain, threshold, learning rate and momentum factor\n'))
    z=eval(input('Use augmented backpropagation? 1-Yes 0-No\n'))
    global EpochMax
    EpochMax=int(input('Max limit on epochs'))
    global inputData                                                            #we cant make changes to global variables without declaring them global
    global outputData
    ann=ANN(x,y,z)
    normalizeData(inputData)                                                    #normalizing data
    normalizeData(outputData)
    if(ann.augbackprop==1):                                                     #augmenting data
        augmentData(inputData)
        augmentData(outputData)
    inputData=inputData[:-1]                                                     #eliminates 'i' or 'o' at end
    outputData=outputData[:-1]    
    computation(ann)                           
                                                   

def feedforward(training_set,layer):
    '''
    Defines relation between different layers of the neural
    Network. Initializes input and output
    '''
    for e in range(len(layer)):
        if e==0:
            layer[e].input(training_set)
            layer[e].output()
        else:
            layer[e].input(layer[e-1].output)                                              #DEBUGGING STATEMENTS
            layer[e].output()
            
    
def backpropagation(ann,layer,oldWeights,epoch,targetOutput):
    
    error=[0]*(ann.outputNodes)
    for i in range(ann.outputNodes):
        error[i]=pow(targetOutput[i]-layer[len(layer)-1].output[i],2)/2.0       
    '''
    print 'Error BackProp : '
    print error
    print '\n'
    '''
    delta=[0]*(ann.outputNodes) 
    for i in range(ann.outputNodes):
        delta[i]=-1*ann.lamb*(targetOutput[i]-layer[len(layer)-1].output[i])*(layer[len(layer)-1].output[i])*(1-layer[len(layer)-1].output[i]) 
    '''
    print 'Del value :'
    print delta
    print '\n' 
    ''' 
    weightChange=[0]*len(ann.weights)
    product=numpy.transpose(numpy.asmatrix(delta))   #nx1 matrix form 
    '''  
    print 'Initial Product'
    print product
    print '\n'
    '''
    for i in range(len(ann.weights)-1,-1,-1):
        a=len(ann.weights)-1
        while(a>=i):                #while loop is used to obtain all weight changes 
            '''
            print 'a : '+str(a)
            print 'i : '+str(i) 
            print '\n'
            '''
            if(a==i):
                '''
                print 'layer[' +str(a) +' ].input'
                print layer[a].input
                print '\n'
                '''
                product=(numpy.asmatrix(layer[a].input))*numpy.transpose(numpy.asmatrix(product))
                weightChange[i]=-1*ann.learnRate*product
                '''
                print 'WeightChange : '+str(i)
                print weightChange[i]
                print '\n'
                '''
                product=numpy.transpose(numpy.asmatrix(delta))
                break
            else:
                s1=numpy.asmatrix(ann.weights[a])*numpy.asmatrix(product)
                '''
                print 's1'
                print s1
                print '\n'
                '''
                s2=[0]*(ann.flat_list[a])
                '''
                print 's2'
                print s2
                print '\n'
                print 'layer[' +str(a) +' ].input'
                print layer[a].input
                print '\n'
                '''
                for e in range(ann.flat_list[a]):
                    '''
                    print 'Range ann.flat_list\n'
                    print ann.flat_list[a]
                    print '\n'
                    
                    '''
                    s2[e]=ann.lamb*(numpy.array(s1).flatten().tolist()[e])*(numpy.array(layer[a].input).flatten().tolist()[e])*(1-numpy.array(layer[a].input).flatten().tolist()[e])
                product=numpy.transpose(numpy.asmatrix(s2))
                '''
                print 'Product :'
                print product
                print '\n'
                '''
                a-=1           
    if(epoch==0):
        for e in range(len(ann.weights)):
            '''
            print 'Weight : '+str(e)
            print  ann.weights[e]
            print '\n'
            '''
            ann.weights[e]+=weightChange[e]  
            '''
            print 'Revised Weight : '+str(e)
            print  ann.weights[e]
            print '\n'
            '''                    
    else:
        for e in range(len(ann.weights)):
            '''
            print 'Weight : '+str(e)
            print  ann.weights[e]
            print '\n'
            '''
            ann.weights[e]=ann.weights[e]+weightChange[e]+ann.alpha*oldWeights[e] 
            '''
            print 'Revised Weight : '+str(e)
            print  ann.weights[e]
            print '\n' 
            '''                      
    oldWeights=weightChange
    '''
    print 'Old Weights change'
    print oldWeights
    print '\n'
    '''
    #ann.alpha*=0.99998
    #ann.learnRate*=0.99998
    return oldWeights
        
    
def ErrorPerFrequency():
    '''
    Calculates error for each individual frequency
    '''
    global ErrorFrequency
    global inputData
    global outputData
    error_per_height=0
    f=range(1000,6600,400)
    f.insert(0,800)
    for i in range(len(f)):
        f[i]/=maxNormalIP[1]
    heightPerFrequency=[0]*len(f)
    t=0
    for i in inputData:
        if(i[1] in f):
            t=f.index(i[1])
            NNoutput=verifyError(i)
            error_per_height=abs((NNoutput-(outputData[inputData.index(i)][0]*maxNormalOP[0]))/(outputData[inputData.index(i)][0]*maxNormalOP[0]))
            ErrorFrequency[t]+=error_per_height
            heightPerFrequency[t]+=1
    for i in range(len(ErrorFrequency)):
        ErrorFrequency[i]/=heightPerFrequency[i]   
    return ErrorFrequency                     
        
    

def ErrorCalculation(ann,layer,target):
    '''
    Calculates error for given epoch across entire training set
    The error for each output node is summed and stored according
    to corresponding index for given epoch
    Plots Error vs Frequency
    '''
    global error_index
    global Error
    error_per_iteration=0
    error1=[0]*(ann.outputNodes)
    for i in range(ann.outputNodes):
        error1[i]=pow(target[i]-layer[len(layer)-1].output[i],2)/2.0
        error_per_iteration+=error1[i]  
    Error[error_index]+=error_per_iteration
    error_per_iteration=0    
            

def verifyError(we):
    global FinalWeight
    x=[4,8,4,1] 
    y=[1,0,0.6,0.9]
    z=0
    ann1=ANN(x,y,z)
    layer=[]
    for t in range(len(ann1.flat_list)):                                         #creates objects for each layer
        layer.append(Layers(t,ann1))
    ann1.weights=FinalWeight           
    inData=we     
    for e in range(len(layer)):
        if e==0:
            layer[e].input(inData)
            layer[e].output()
        else:
            layer[e].input(layer[e-1].output)                                              #DEBUGGING STATEMENTS
            layer[e].output()
    for e in range(len(maxNormalOP)-1):                                                   #Remove -1 for general purpose application
       output=layer[len(layer)-1].output[e]*maxNormalOP[e]
    return output


def verify(we):
    global FinalWeight
    x=eval(input('Enter number of neurons in input, hidden(s) and ouput layer'))  
    y=eval(input('Enter sigmoidal gain, threshold, learning rate and momentum factor'))
    z=eval(input('Use augmented backpropagation? 1-Yes 0-No'))
    ann1=ANN(x,y,z)
    layer=[]
    for t in range(len(ann1.flat_list)):                                         #creates objects for each layer
        layer.append(Layers(t,ann1))
    if (we==1):    
        for e in range(len(ann1.weights)):
            ann1.weights[e]=numpy.asmatrix(eval(input('Enter weight ['+str(e)+'] in list form:')))
    else:
        ann1.weights=FinalWeight           
    inData=eval(input('Give input in simple list unnormalized form, APPEND "i"'))
    for e in range(len(inData[0])):
        inData[0][e]/=maxNormalIP[e]   
    if(ann1.augbackprop==1):                                                     #augmenting data
        augmentData(inData) 
    inData=inData[0]     
    for e in range(len(layer)):
        if e==0:
            layer[e].input(inData)
            layer[e].output()
        else:
            layer[e].input(layer[e-1].output)                                              #DEBUGGING STATEMENTS
            layer[e].output()
    for e in range(len(maxNormalIP)):        
        print('Input Value :(NOT normalized)')
        if(ann1.augbackprop==1):
            print(inData[3*e]*maxNormalIP[e])
        else:
            print(inData[e]*maxNormalIP[e])     
    print('\n')
    for e in range(len(maxNormalOP)):           
        print('Output Value :(NOT normalized)')
        if(ann1.augbackprop==1):
            print(layer[len(layer)-1].output[3*e]*maxNormalOP[e])
        else:
            print(layer[len(layer)-1].output[e]*maxNormalOP[e]) 
            
                            
def computation(ann):
    '''
    Initializes iteration and epoch values
    Stores previous weight change values
    Creates new layers for each iteration
    '''
    global FinalWeight
    global error_index                                                                 #References to Error list
    epoch=0
    iteration=0
    oldWeights=0
    while(epoch<=EpochMax):
        for e in range(len(inputData)):
            layer=[]
            for t in range(len(ann.flat_list)):                                         #creates objects for each layer
                layer.append(Layers(t,ann))
            '''
            print 'input data'
            print inputData[e]
            print '\n' 
            '''
            feedforward(inputData[e],layer)
            if(epoch%1000==0):                                                          #Calculates error for every 1000th epoch
                ErrorCalculation(ann,layer,outputData[e])
            oldWeights=backpropagation(ann,layer,oldWeights,epoch,outputData[e])
            iteration+=1
            #print('iteration: '+str(iteration))
            #print('\n')
            del layer
        if(epoch%1000==0):    
            error_index+=1
        epoch+=1 
        print('epoch: '+str(epoch))
        print('\n')
    for i in range(len(ann.weights)):
        print('Weight final '+str(i))
        print(ann.weights[i])
        print('\n')    
    FinalWeight=ann.weights
    #WEIGHTS FOR COMPACT CMSA - 40K epochs
    #FinalWeight[0]=numpy.asmatrix([[ -0.43895495, -0.64924281,  0.14109208,  0.69548946,  0.71918986,  0.8254113, 1.72226988, -0.13677951],[ 0.42397634,  0.15306859,  0.99310132,  1.46362207,  0.43528094, -0.69663305, 2.1639061,   0.2357818],[  1.480957,    1.73959711,  0.55829586, -2.02752574,  0.79403914,  1.85371923, -2.14041245,  0.36581561],[ -0.63624157, -2.45188231,  0.67745236,  0.1248758,   0.15718808, -1.36619911, -1.36552918,  0.59295538]])
    #FinalWeight[1]=numpy.asmatrix([[ -0.13794039,  0.65144523, -1.50487576, -0.73868314],[ 0.13384244,  0.85422409, -2.8560473,  -1.9277813],[ -0.02662097,  0.69197758, -0.75293664,  0.35929862],[ -0.59346261,  0.46813441,  2.17067891,  2.64849459],[ -0.34012121,  0.24840122, -1.25577835,  0.22037885],[  0.16012434,  1.22077375, -2.81000528, -0.9787289],[ 0.23980144,  0.02568168,  3.16953112,  3.30605906],[  -0.10775494,  0.81115453, -0.72610513,  0.50648311]])
    #FinalWeight[2]=numpy.asmatrix([[ 0.57824946],[ 4.06468669],[-5.25133157],[-4.7352063 ]])
script()