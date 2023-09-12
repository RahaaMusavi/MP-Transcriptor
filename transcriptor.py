
# import pandas lib as pd
import pandas as pd

#sttructuring dataframe according to the two required columns:
#col4 = transcription and col5 = transliteration
require_cols = [4, 5]
required_df = pd.read_excel('chart.xlsx', usecols = require_cols)

#dropping empty cells
df = required_df.dropna ()

#dropping cells starting with # from both columns
df = df[~df[['transliteration','transcription']].astype(str).str.startswith('#')]
##df = df[~df['transcription'].astype(str).str.startswith('#')]



#The problem with alternating line text was that it was difficult to connect two lines seq2seq.
##aod = pd.read_fwf("AOD.txt", sep = ' ')
##print (aod)
