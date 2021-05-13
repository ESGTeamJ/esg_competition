'''Assigning values from one database to another where some amount of
companies are found in both databases but may not have identical name of the company.
e.g. in first database:"3M" in second:"3M Co" and now we woul like to connect values from both 
databases and evaluate company 3M.'''
'''For this we need to import esential libraries'''
from fuzzywuzzy import process
from cleanco import cleanco
import pandas as pd
from tqdm import tqdm

'''Add path to a .xlsx or .csv file where data are already transpose (output from wordsSearching.py or htmlDownloader.py 
but data are splitted in to a separated cells by delimiter by quick .csv/.xslx function transpose )'''
df1_path = 'D:\Desktop\Analysis\pledgers.xlsx'

df1 = pd.read_excel(df1_path)
df1 = df1.reset_index(drop=True)
'''It takes every string under "Company Name" and add it to list.'''
companies = df1['Company Name'].apply(cleanco, 0)
companies = companies.apply(lambda x: x.clean_name())
companies = companies.apply(lambda x: x.lower())
companies = companies.tolist()

'''Add path to a second database which you want to match with the first 
one (data must be also formated/transpose) '''
df2_path = 'D:\Desktop\Analysis\initData.xlsx'

df2 = pd.read_excel(df2_path)
df2 = df2.reset_index(drop=True)

companies_dest = df2['Company Name'].apply(cleanco, 0)
companies_dest = companies_dest.apply(lambda x: x.clean_name())
companies_dest = companies_dest.apply(lambda x: x.lower())
companies_dest = companies_dest.tolist()

'''Aplying fuzzy name matchin'''
results = []
number_of_matches = 1
for idx, company in enumerate(tqdm(companies)):
    '''res1 is result of matching names of companies in % (0-100)'''
    res1 = process.extract(company, companies_dest, limit=number_of_matches)[0]

    '''defining data that should be extracted from second database by header 
    name in .csv or .xslx file.(It takes values that are under the header..)'''
    index = companies_dest.index(res1[0])
    company_name = df2.iloc[index]['Company Name']
    isin = df2.iloc[index]['Identifier (ISIN)']
    
    '''Values that should be displayed as a result'''
    results.append([company_name, isin, res1[1]])
    
'''Setting up custom header under which will be displayed data from company_name, isin,res1[1]'''
results = pd.DataFrame(results, columns=['company_name', 'isin', 'score'], index=df1.index)

'''Creating which data should be extracted from database1 by header name in .csv or .xslx'''
final_results = pd.concat(
    [results, df1['Company Name'], df1['Science Based Targets initiative'], df1['RE100 - 100% renewable power'],
     df1['EP100 - Commit to smart energy use'], df1['Responsible climate policy'],
     df1['Report climate change information'], df1['EV100 - Commit to electric vehicles'], df1['No. Diff pledges']],
    axis=1)

'''In final .csv file we want to write only those which score of matching will be greater then 
some nunmber, in our case 90+ was very effective '''
is_gt_90 = final_results['score'] > 90
final_results = final_results[is_gt_90]

'''Add path and name for your final output .csv file'''
final_results.to_csv('D:/Desktop/nameMatch/pledgers90+.csv', index=False)
