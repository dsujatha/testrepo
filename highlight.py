import pandas as pd



df = pd.read_excel('my-diff-2.xlsx', 'changed', na_values=['NA'])
#df = pd.DataFrame([[2,3,1], [3,2,2], [2,4,4]], columns=list("ABC"))


def highlight_differences(val):
    print(val)
    color = 'yellow' if "--->" in str(val) else 'white'
    return 'background-color: %s' % color



df.style.\
    applymap(highlight_differences).\
    to_excel('output.xlsx', engine='xlsxwriter', index=False)

print('Done')