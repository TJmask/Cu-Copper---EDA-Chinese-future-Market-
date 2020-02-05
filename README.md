# Cu-EDA
This is about the eda of Copper in China Futures Market
## Outline
### basic description 
1. rows, max, min, duplicates, outliers?
2. daily and nights commodity futures,compare. when? period? amount? price?  

### Analysis
1. time series AR(1), AR(2)
2. holiday analysis, after and before holiday, price, amount. (holiday lists)(how about friday and monday?)
3. compare different time/trading period, morning, afternoon, as well as friday nights, any significant difference?
4. index analysis, MACD,DMA,CR?? there are so many indexs, which one should I choose?
5. period analysis 1 min, 2 mins, 5 mins, 10 mins? which period has the highest profits interval?

### feature analysis
1. feature lists pandas_ta
2. analyze each feature and see if it's important
3. (there are overlaps of index analysis) https://github.com/twopirllc/pandas-ta

### comparison with other futures
1. correlation analysis
2. crossover analysis

### statistical analysis
1. HMM
2. Fourier

### some hypothesis 
1. different time/trading period has significant impact on price and amount
2. holiday might have impact on price
3. firday or monday might have impact as well 
4. breaks(big events) should have impact 

### summary
1. which features are important
2. what conclusion are useful for futrue analysis
