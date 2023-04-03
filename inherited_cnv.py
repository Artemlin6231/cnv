import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sys
matplotlib.use('Agg')
args = sys.argv
file1 = sys.argv[1]
file2 = sys.argv[2]
file_child = sys.argv[3]
n = sys.argv[4]
name = sys.argv[5]
df_parent1 = pd.read_csv(file1, sep = '\t')
df_parent2 = pd.read_csv(file2, sep = '\t')
df_child = pd.read_csv(file_child, sep = '\t')
def plot_inherited_from_freq(file1,file2,file_child,name):
    df_parent1 = pd.read_csv(file1, sep='\t')
    df_parent2 = pd.read_csv(file2, sep='\t')
    df_child = pd.read_csv(file_child, sep='\t')
    accuracy = []
    freq = []
    for n in range(10,1000,1):
        n = n/1000
        df_parent1_freq = df_parent1.loc[df_parent1['freq']<n]
        df_parent2_freq = df_parent2.loc[df_parent2['freq']<n]
        df_child_freq = df_child.loc[df_child['freq']<n]
        is_inherited_from_mother_start = df_child_freq['start'].isin(df_parent1_freq['start']).to_frame()
        is_inherited_from_mother_end = df_child_freq['end'].isin(df_parent1_freq['end']).to_frame()
        is_inherited_from_mother_status = df_child_freq['status'].isin(df_parent1_freq['status']).to_frame()
        is_inherited_from_mother_startend = is_inherited_from_mother_start['start'].isin(is_inherited_from_mother_end['end']).to_frame()
        is_inherited_from_mother = is_inherited_from_mother_startend['start'].isin(is_inherited_from_mother_status['status']).to_frame()
        is_inherited_from_mother['start'] = is_inherited_from_mother['start']*is_inherited_from_mother_start['start']

        is_inherited_from_father_start = df_child_freq['start'].isin(df_parent2_freq['start']).to_frame()
        is_inherited_from_father_end = df_child_freq['end'].isin(df_parent2_freq['end']).to_frame()
        is_inherited_from_father_status = df_child_freq['status'].isin(df_parent2_freq['status']).to_frame()
        is_inherited_from_father_startend = is_inherited_from_father_start['start'].isin(is_inherited_from_father_end['end']).to_frame()
        is_inherited_from_father = is_inherited_from_father_startend['start'].isin(is_inherited_from_father_status['status']).to_frame()
        is_inherited_from_father['start'] = is_inherited_from_father['start']*is_inherited_from_father_start['start']

        final = (is_inherited_from_father['start']+is_inherited_from_mother_start['start']).to_frame()
        x = final['start'].sum()/len(final)
        freq.append(n)
        accuracy.append(x)
    plt.plot(freq,accuracy)
    plt.xlabel('Максимальная частота')
    plt.ylabel('Процент cnv от родителей')
    gr_name = name + '.pdf'
    plt.savefig(gr_name )
def uninherited_cnv(file1,file2,file_child,n,name):
    df_parent1 = pd.read_csv(file1, sep='\t')
    df_parent2 = pd.read_csv(file2, sep='\t')
    df_child = pd.read_csv(file_child, sep='\t')
    df_parent1_freq = df_parent1.loc[df_parent1['freq']<n]
    df_parent2_freq = df_parent2.loc[df_parent2['freq']<n]
    df_child_freq = df_child.loc[df_child['freq']<n]
    is_inherited_from_mother_start = df_child_freq['start'].isin(df_parent1_freq['start']).to_frame()
    is_inherited_from_mother_end = df_child_freq['end'].isin(df_parent1_freq['end']).to_frame()
    is_inherited_from_mother_status = df_child_freq['status'].isin(df_parent1_freq['status']).to_frame()
    is_inherited_from_mother_startend = is_inherited_from_mother_start['start'].isin(is_inherited_from_mother_end['end']).to_frame()
    is_inherited_from_mother = is_inherited_from_mother_startend['start'].isin(is_inherited_from_mother_status['status']).to_frame()
    is_inherited_from_mother['start'] = is_inherited_from_mother['start']*is_inherited_from_mother_start['start']

    is_inherited_from_father_start = df_child_freq['start'].isin(df_parent2_freq['start']).to_frame()
    is_inherited_from_father_end = df_child_freq['end'].isin(df_parent2_freq['end']).to_frame()
    is_inherited_from_father_status = df_child_freq['status'].isin(df_parent2_freq['status']).to_frame()
    is_inherited_from_father_startend = is_inherited_from_father_start['start'].isin(is_inherited_from_father_end['end']).to_frame()
    is_inherited_from_father = is_inherited_from_father_startend['start'].isin(is_inherited_from_father_status['status']).to_frame()
    is_inherited_from_father['start'] = is_inherited_from_father['start']*is_inherited_from_father_start['start']
    final = (is_inherited_from_father['start']+is_inherited_from_mother_start['start']).to_frame()
    x = final['start'].sum()/len(final)
    final = final.rename(columns={'start': 'inherited'})
    df_child_freq = pd.concat([df_child_freq, final], axis=1)
    un_inherited = df_child_freq.loc[df_child_freq['inherited'] == False]
    gr_name = 'un_inherited' + name + '.csv'
    un_inherited.to_csv(gr_name, index=False)
plot_inherited_from_freq(file1,file2,file_child,name)
uninherited_cnv(file1,file2,file_child,n,name)
