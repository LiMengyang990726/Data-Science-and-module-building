# Kernal Learning Journal
## 1. House price Kernal
- *Figure out outliers* (Through the most obvious relationship: area & price)

    -- `fig,ax = plt.subplots` is commonly used even if there is only one simple plot that needs to be plotted. It is useful if you want to change figure-level attributes or save the figure as an image file later. e.g.`fig.savefig('yourfilename.png')`

    -- `lambda` function: lambda functionSpecifier(params): things to return
- *Fit the target into a observed funtion*

  -- Useful functions to visualize:  `sns.distplot`, `stats.probplot`
  -- Fit into a linear line, can try `np.log1p(xxx)` (log(1+x))

- *Feature Engineering*

  -- Combine `train` set and `test` set -> Make all the missing data into a DataFrame according to the percentage
    `all_data_na = (all_data.isnull().sum() / len(all_data)) * 100`,
    `all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:col]`

  -- See the corrolation: `corrmat = all_data.corr()`, then use `sns.heatmap()`

  -- Fill missing values:

     a) Fill with None / other values according to the physical meaning
     b) Fill it with some arithmetic operations like: fill with certain value through grouping. E.g. `df.groupby(col2)[col1].transform(lambda x: x.fillna(x.median()))`
     c) Fill with
