{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\\begin{align*}\n",
    "X_i|p & \\sim \\text{Binomial}(n,p)\\\\\n",
    "p & \\sim \\text{Beta}(a, b)\n",
    "\\end{align*}\n",
    "\n",
    "$$Q(\\tau)=\\beta_0(\\tau) + \\beta_1(\\tau) X_1 + \\cdots + \\beta_p(\\tau) X_p,$$\n",
    "\n",
    "$$ S = \\sum_{i=1}^{n} \\rho_{\\tau}(Y_i - \\hat{Q}_i(\\tau)), $$\n",
    "where $Y_i$ for $i=1,\\ldots,n$ is the response data, $\\hat{Q}_i(\\tau)$ are the $\\tau$-quantile estimates, and $\\rho_{\\tau}$ is the __check function__ (also known as the _absolute asymmetric deviation function_ or _tick function_), given by\n",
    "$$ \\rho_{\\tau}(s) = (\\tau - I(s<0))s $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# reference https://github.com/pandas-dev/pandas/blob/v0.24.1/pandas/core/generic.py#L9484-L9815\n",
    "#find most common item in a list\n",
    "from collections import Counter\n",
    "\n",
    "def Most_Common(lst):\n",
    "    data = Counter(lst)\n",
    "    return data.most_common(1)[0][0]\n",
    "#what to do in case of ties?\n",
    "\n",
    "Most_Common([\"hello\", \"hello\", 1, 3, 5])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>sale</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2012</td>\n",
       "      <td>55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4</td>\n",
       "      <td>2014</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7</td>\n",
       "      <td>2013</td>\n",
       "      <td>84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Nan</td>\n",
       "      <td>2014</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  month  year  sale\n",
       "0     1  2012    55\n",
       "1     4  2014    40\n",
       "2     7  2013    84\n",
       "3   Nan  2014    31\n",
       "4    11  2015    11"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=pd.DataFrame({'month': [1, 4, 7, 'Nan', 11],\n",
    "                   'year': [2012, 2014, 2013, 2014, 2015],\n",
    "                   'sale': [55, 40, 84, 31, 11]})\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2012 55]\n",
      "0\n",
      "[4 2014 40]\n",
      "0\n",
      "[7 2013 84]\n",
      "0\n",
      "[dtype('O'), dtype('O'), dtype('O')]\n",
      "yes\n"
     ]
    }
   ],
   "source": [
    "column_range= np.arange(0, data.shape[1])\n",
    "list_of_types=[]\n",
    "for column_index in column_range:\n",
    "    #access column values\n",
    "    col_vals= data.values[column_index]\n",
    "    print(col_vals)\n",
    "    list_of_types.append(col_vals.dtype)\n",
    "    #col_vals.value_counts(dropna = False)[np.nan]\n",
    "    #find nas\n",
    "    col_df= data.iloc[:, column_index]\n",
    "    count_NAs = col_df.isna().sum()\n",
    "    print(count_NAs)\n",
    "print(list_of_types)\n",
    "if Most_Common(list_of_types) == 'float64' or 'int64':\n",
    "    print(\"yes\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-86bb8ebfe154>, line 83)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-86bb8ebfe154>\"\u001b[1;36m, line \u001b[1;32m83\u001b[0m\n\u001b[1;33m    return pd.DataFrame({}: )\u001b[0m\n\u001b[1;37m                          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#write summary function\n",
    "def summary(data):\n",
    "    '''\n",
    "    This function computes summary statistics for text and numerical data from a given dataframe.\n",
    "    \n",
    "    Input: dictionary or dataframe\n",
    "    \n",
    "    Returns summary statistics for each column in a nested pandas dataframe. It will determine the main data type of the column\n",
    "    by calculated the type of each row entry in the column, and using the most frequent data type as the expected input for \n",
    "    that column. \n",
    "    It will perform two different summary statistics based on 2 different groups of datatypes of either\n",
    "    1) string or 2) int/float. For number columns it returns a dictionary of summary statistics including\n",
    "    mean value for each column, min, max, count (number of non NA values per column) and count_NA \n",
    "    (number of NA values per column). Similarly, for string columns it returns the unique string values and \n",
    "    their counts in a dictionary. It will also provide a count of NA values which will include empty strings,\n",
    "    and anything other than the correct data type for each column. The column summary statistics are then nested\n",
    "    into a larger dataframe.\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    data : dataframe\n",
    "        This is the dataframe that the function will use to provide summary statistics of each column in the data frame. \n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    Summary table of each columns summary statistics\n",
    "    \n",
    "    >>> summary(pd.DataFrame(colnames=”Likes coding”, rows= np.array([[4,3,2, 2])))\n",
    "    pd.DataFrame{('col1', values=\n",
    "        min= 2\n",
    "        max= 4\n",
    "        mean= 11/4\n",
    "        median= 2\n",
    "        count= 4\n",
    "        count_NA= 0\n",
    "        unique= [4,3,2])}\n",
    "\n",
    "    '''\n",
    "    #check that input is a pandas df\n",
    "    if type(data) != type(pd.DataFrame({'Val': 1})):\n",
    "        return print(\"Please input data as a pandas dataframe using pd.DataFrame(data)\")\n",
    "    \n",
    "    # check dimensions\n",
    "    if data.ndim >= 3:\n",
    "        msg = \"summary is not implemented on Panel objects.\"\n",
    "        raise NotImplementedError(msg)\n",
    "\n",
    "    elif data.ndim == 2 and data.columns.size == 0:\n",
    "        raise ValueError(\"Cannot describe a DataFrame without columns\")\n",
    "    \n",
    "    #check type of each data column to determine which analysis to do\n",
    "    def describe_1d(data):\n",
    "\n",
    "            if is_bool_dtype(data):\n",
    "\n",
    "                return summary_categorical_1d(data)\n",
    "\n",
    "            elif is_numeric_dtype(data):\n",
    "\n",
    "                return summary_numeric_1d(data)\n",
    "\n",
    "            elif is_timedelta64_dtype(data):\n",
    "\n",
    "                return summary_numeric_1d(data)\n",
    "\n",
    "            else:\n",
    "\n",
    "                return summary_categorical_1d(data)\n",
    "    \n",
    "    def summary_numeric_1d(data):\n",
    "        stat_index = (['count', 'count_NAs' 'mean', 'std', 'min', 'max'])\n",
    "\n",
    "        d = ([series.count(), col_df.isna().sum(), series.mean(), series.std(), series.min()] + [series.max()])\n",
    "\n",
    "        column_range= np.arange(0, data.shape[1])\n",
    "    \n",
    "        for column_index in column_range:\n",
    "        #access column\n",
    "            col_vals= data.values[:,column_index]\n",
    "            col_df= data.iloc[:, column_index]\n",
    "            count_NAs = col_df.isna().sum()\n",
    "            min_ = np.min(col_vals)\n",
    "            max_ = np.max(col_vals)\n",
    "            mean = np.mean(col_vals)\n",
    "            median = np.median(col_vals)\n",
    "            count= len(col_vals)\n",
    "    return pd.DataFrame({stat_index}: d )\n",
    "    #return pd.Series(d, index=stat_index, name=series.name)\n",
    "\n",
    "\n",
    "    \n",
    "    def summary_categorical_1d(data):\n",
    "        column_range= np.arange(0, data.shape[1])\n",
    "    \n",
    "        for column_index in column_range:\n",
    "        #access column\n",
    "        count=      \n",
    "\n",
    "        unique =    \n",
    "\n",
    "        top         \n",
    "\n",
    "        freq "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "    def summary_numeric_1d(col_vals):\n",
    "\n",
    "        stat_index = (['count', 'mean', 'std', 'min', 'count_NAs', 'unique'] \n",
    "\n",
    "        d = ([col_vals.count(), col_vals.mean(), col_vals.std(), col_vals.min(), col_df.is_na.sum()])\n",
    "\n",
    "        return pd.DataFrame(d, index=stat_index)\n",
    "                    \n",
    "\n",
    "    def summary_categorical_1d(col_vals):\n",
    "        names = ['count', 'unique', 'count_NAs']\n",
    "\n",
    "        objcounts = col.value_counts()\n",
    "\n",
    "        count_unique = len(objcounts[objcounts != 0])\n",
    "            \n",
    "        count_NAs = count\n",
    "\n",
    "        result = [data.count(), count_unique, count_NAs]\n",
    "\n",
    "        if result[1] > 0:\n",
    "\n",
    "        top, freq = objcounts.index[0], objcounts.iloc[0]\n",
    "\n",
    "\n",
    "\n",
    "    if is_datetime64_any_dtype(col_vals):\n",
    "\n",
    "        tz = data.dt.tz\n",
    "\n",
    "        asint = data.dropna().values.view('i8')\n",
    "\n",
    "        top = Timestamp(top)\n",
    "\n",
    "    if top.tzinfo is not None and tz is not None:\n",
    "\n",
    "    # Don't tz_localize(None) if key is already tz-aware\n",
    "\n",
    "        top = top.tz_convert(tz)\n",
    "\n",
    "    else:\n",
    "\n",
    "        top = top.tz_localize(tz)\n",
    "\n",
    "        names += ['top', 'freq', 'first', 'last']\n",
    "\n",
    "        result += [top, freq,\n",
    "\n",
    "                 Timestamp(asint.min(), tz=tz),\n",
    "\n",
    "                 Timestamp(asint.max(), tz=tz)]\n",
    "\n",
    "    else:\n",
    "\n",
    "        names += ['top', 'freq']\n",
    "\n",
    "        result += [top, freq]\n",
    "\n",
    "\n",
    "\n",
    "    return pd.Series(result, index=names, name=data.name)\n",
    "\n",
    "\n",
    "    #determine which data type each column is and the corresponding analysis needed\n",
    "    def summary_1d(col):\n",
    "\n",
    "        if Most_Common(list_of_types) == 'float64' or 'int64':\n",
    "\n",
    "            return summary_numeric_1d(col)\n",
    "\n",
    "        elif Most_Common(list_of_types) ==  'timedelta64':\n",
    "\n",
    "            return summary_numeric_1d(col)\n",
    "\n",
    "        elif Most_Common(list_of_types) == 'bool':\n",
    "            return summary_categorical_1d(col)\n",
    "            \n",
    "        else:\n",
    "            return summary_categorical_1d(col)\n",
    "            \n",
    "\n",
    "\n",
    "        \n",
    "#find min, max, median and mean and count \n",
    "  \n",
    "    #df['Min'], df['Max'] = df['Val'].min(), df['Val'].max()\n",
    "    #find number of NAs\n",
    "                \n",
    "    #make nested df\n",
    "    #for result in results\n",
    "    #nested = pd.DataFrame({as.string(result)}, values..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 15)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<tokenize>\"\u001b[1;36m, line \u001b[1;32m15\u001b[0m\n\u001b[1;33m    def describe_categorical_1d(data):\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "        if self.ndim == 1:\n",
    "\n",
    "            return describe_1d(self)\n",
    "\n",
    "        elif (include is None) and (exclude is None):\n",
    "\n",
    "            # when some numerics are found, keep only numerics\n",
    "\n",
    "            data = self.select_dtypes(include=[np.number])\n",
    "\n",
    "            if len(data.columns) == 0:\n",
    "\n",
    "                data = self\n",
    "\n",
    "        elif include == 'all':\n",
    "\n",
    "            if exclude is not None:\n",
    "\n",
    "                msg = \"exclude must be None when include is 'all'\"\n",
    "\n",
    "                raise ValueError(msg)\n",
    "\n",
    "            data = self\n",
    "\n",
    "        else:\n",
    "\n",
    "            data = self.select_dtypes(include=include, exclude=exclude)\n",
    "\n",
    "\n",
    "\n",
    "        ldesc = [describe_1d(s) for _, s in data.iteritems()]\n",
    "\n",
    "        # set a convenient order for rows\n",
    "\n",
    "        names = []\n",
    "\n",
    "        ldesc_indexes = sorted((x.index for x in ldesc), key=len)\n",
    "\n",
    "        for idxnames in ldesc_indexes:\n",
    "\n",
    "            for name in idxnames:\n",
    "\n",
    "                if name not in names:\n",
    "\n",
    "                    names.append(name)\n",
    "\n",
    "\n",
    "\n",
    "        d = pd.concat(ldesc, join_axes=pd.Index([names]), axis=1)\n",
    "\n",
    "        d.columns = data.columns.copy()\n",
    "\n",
    "        return d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Val</th>\n",
       "      <th>Min</th>\n",
       "      <th>Max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Val  Min  Max\n",
       "0    1    1    3\n",
       "1    3    1    3\n",
       "2    1    1    3\n",
       "3    2    1    3\n",
       "4    2    1    3\n",
       "5    3    1    3"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "df = pd.DataFrame({'Val':np.random.randint(1,6,6)})\n",
    "df['Min'], df['Max'] = df['Val'].min(), df['Val'].max()\n",
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
