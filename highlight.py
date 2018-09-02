import pandas as pd



df = pd.read_excel('my-diff-2.xlsx', 'changed', na_values=['NA'])
#df = pd.DataFrame([[2,3,1], [3,2,2], [2,4,4]], columns=list("ABC"))


def highlight_differences(val):
    print(val)
    color = 'yellow' if "--->" in str(val) else 'white'
    return 'background-color: %s' % color

  

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 3 else 'black'
    return 'color: %s' % color

#df.style.apply(lambda x: ["background: red" if v > x.iloc[0] else "" for v in x], axis = 1)
#print(df)




df.style.\
    applymap(highlight_differences).\
    to_excel('output.xlsx', engine='xlsxwriter', index=False)

print('Done')