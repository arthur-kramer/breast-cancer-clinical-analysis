# ---------   Importing Libraries   ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, mannwhitneyu, chi2_contingency

# ---------   Database Import and Processing   ----------

!pip install -q gdown
!gdown --id 1VRgMRU8AprDoWOlqxGY5O8ZJFeQ8cNzT --output breast-cancer-dataset.csv

df = pd.read_csv('breast-cancer-dataset.csv')

# Tratando a coluna 'Age'
df.loc[:, 'Age'] = pd.to_numeric(df['Age'], errors='coerce')
df = df.dropna(subset=['Age'])
df['Age'] = df['Age'].astype('int64')

# Tratando a coluna 'Tumor Size (cm)'
df.loc[:, 'Tumor Size (cm)'] = pd.to_numeric(df['Tumor Size (cm)'], errors='coerce')
df = df.dropna(subset=['Tumor Size (cm)'])
df['Tumor Size (cm)'] = df['Tumor Size (cm)'].astype('int64')

# Tratando a coluna 'History'
df.loc[:, 'History'] = pd.to_numeric(df['History'], errors='coerce')
df = df.dropna(subset=['History'])
df['History'] = df['History'].astype('object')

# Removendo colunas indesejadas
df.drop(columns=['S/N', 'Year', 'Breast Quadrant'], inplace=True)

# Ajustando tipo de Menopause para categórico
df['Menopause'] = df['Menopause'].astype('object')

# ---------   General Data Analysis   ----------

def check_df(dataframe):
    print(" SHAPE ".center(80,'~'))
    print(dataframe.shape)
    print(" TYPES ".center(80,'~'))
    print(dataframe.dtypes)
    print(" HEAD ".center(80,'~'))
    print(dataframe.head())
    print(" MISSING VALUES ".center(80,'~'))
    print(dataframe.isnull().sum())
    print(" DESCRIBE ".center(80,'~'))
    print(dataframe.describe().T)

check_df(df)

# ---------   Normality Tests   ----------

# Normality test - Age
alpha = 0.05

stat, p = shapiro(df['Age'])
print(f'\n[Testando a normalidade da variável "Idade"]\n\nEstatística W = {stat:.4f}\np-valor = {p:.4f}\n')
print("→ Distribuição é aproximadamente normal." if p > 0.05 else "→ Distribuição não é normal.")

# Normality test - Tumor Size
alpha = 0.05

stat, p = shapiro(df['Tumor Size (cm)'])
print(f'\n[Testando a normalidade da variável "Tamanho do Tumor"]\n\nEstatística W = {stat:.4f}\np-valor = {p:.8f}\n')
print("→ Distribuição é aproximadamente normal." if p > 0.05 else "→ Distribuição não é normal.")

# ---------   Exploratory Analysis   ----------

# Histogram and Boxplot of Age
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Cases')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Age'])
plt.title('Age Boxplot')
plt.xlabel('Age')
plt.tight_layout()
plt.show()

# Histogram and Boxplot of Tumor Size
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Tumor Size (cm)'], kde=True)
plt.title('Tumor Size Distribution')
plt.xlabel('Tumor Size (cm)')
plt.ylabel('Number of Cases')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Tumor Size (cm)'])
plt.title('Tumor Size Boxplot')
plt.xlabel('Tumor Size (cm)')
plt.tight_layout()
plt.show()

# Boxplot of Tumor Size by Diagnosis
plt.figure(figsize=(8, 6))
sns.boxplot(
    x='Diagnosis Result',
    y='Tumor Size (cm)',
    data=df,
    hue='Diagnosis Result',
    palette={'Benign':'green', 'Malignant':'red'})
plt.title('Boxplot of Tumor Size by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Tumor Size (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot of Age by Diagnosis
plt.figure(figsize=(8, 6))
sns.boxplot(
    x='Diagnosis Result',
    y='Age',
    data=df,
    hue='Diagnosis Result',
    palette={'Benign':'green', 'Malignant':'red'})
plt.title('Boxplot of Age by Diagnosis')
plt.ylabel('Idade')
plt.xlabel('Diagnosis')
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot of Tumor Size by Family History
df['Historico'] = df['History'].map({0: 'Without history', 1: 'With history'})

plt.figure(figsize=(8, 6))
sns.boxplot(
    x='Historico',
    y='Tumor Size (cm)',
    data=df,
    hue='Historico',
    palette=["#6B6B6B", '#5152A1'])
plt.title('Boxplot of Tumor Size by Family History')
plt.xlabel('Family History')
plt.ylabel('Tumor Size (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Proportion of Family History by Diagnosis
# Criando a tabela de proporções
cross_tab = pd.crosstab(df['Diagnosis Result'], df['History'], normalize='index')

# Plotando
ax = cross_tab.plot(kind='bar', stacked=True, color=["#6B6B6B", '#5152A1'], figsize=(8, 6))
ax.set_xticklabels(['Benign', 'Malignant'], rotation=0)

# Adicionando rótulos de porcentagem dentro das barras
for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        if height > 0.03:  # Evita anotar proporções muito pequenas
            ax.annotate(f'{height*100:.1f}%',
                        (bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        ha='center', va='center', fontsize=10, color='white')

plt.title('Proportion of Family History by Diagnosis')
plt.ylabel('Proportion')
plt.xlabel('Diagnosis', rotation=0)
plt.legend(title='Family History', labels=['Without history', 'With history'])
plt.tight_layout()
plt.show()

# Proportion of Diagnosis by Menopause Status
# Criar tabela de contingência com proporção por linha (status da menopausa)
cross_tab = pd.crosstab(df['Menopause'], df['Diagnosis Result'], normalize='index')

# Plotar gráfico de barras empilhadas
ax = cross_tab.plot(kind='bar', stacked=True, color=["green", 'red'], figsize=(8,6))

# Ajustar rótulos do eixo x
ax.set_xticklabels(['Reached menopause', 'Not reached menopause'], rotation=0)

# Adicionando rótulos de porcentagem dentro das barras
for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        if height > 0.03:  # Evita anotar proporções muito pequenas
            ax.annotate(f'{height*100:.1f}%',
                        (bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        ha='center', va='center', fontsize=10, color='white')

plt.title('Proportion of Diagnosis by Menopause Status')
plt.xlabel('Menopause Status')
plt.ylabel('Proportion')
plt.legend(title='Diagnosis')
plt.tight_layout()
plt.show()

# Scatterplot between Age and Tumor Size by Diagnosis
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Tumor Size (cm)', hue='Diagnosis Result', palette={'Benign': 'green', 'Malignant': 'red'})
plt.title('Scatterplot between Age and Tumor Size by Diagnosis')
plt.xlabel('Age')
plt.ylabel('Tumor Size (cm)')
plt.legend(title='Diagnosis')
plt.grid(True)
plt.show()

## ---------   Hypothesis Tests (significance level (α=0.05))   ---------

# Hypothesis 1
    # H0: There is no significant difference in the mean tumor size between patients with benign and malignant diagnoses.
    # H1: There is a significant difference in the mean tumor size between patients with benign and malignant diagnoses.

# Separando os tamanhos dos tumores por grupo de diagnóstico
tumor_benigno = df[df['Diagnosis Result'] == 'Benign']['Tumor Size (cm)']
tumor_maligno = df[df['Diagnosis Result'] == 'Malignant']['Tumor Size (cm)']

# Aplicar o teste de Mann-Whitney
stat, p = mannwhitneyu(tumor_benigno, tumor_maligno, alternative='two-sided')

print(f'Teste de Mann-Whitney - Hipótese 1\n\nEstatística U = {stat:.4f}\np-valor = {p:.5f}\n')

if p < 0.05:
    print("Rejeita-se H0:\nHá evidências para concluir que há diferença significativa no tamanho médio dos tumores entre diagnósticos benignos e malignos.")
else:
    print("Não rejeita-se H0:\nNão há evidências suficientes para concluir que há diferença no tamanho médio dos tumores entre diagnósticos benignos e malignos.")

# Hypothesis 2
    # H0: There is no significant difference in the age of patients with benign and malignant diagnoses.
    # H1: There is a significant difference in the age of patients with benign and malignant diagnoses.

# Separando as idades por grupo de diagnóstico
idades_pacientes_benigno = df[df['Diagnosis Result'] == 'Benign']['Age']
idades_pacientes_maligno = df[df['Diagnosis Result'] == 'Malignant']['Age']

# Aplicar o teste de Mann-Whitney
stat, p = mannwhitneyu(idades_pacientes_benigno, idades_pacientes_maligno, alternative='two-sided')

print(f'Teste de Mann-Whitney - Hipótese 2\n\nEstatística U = {stat:.4f}\np-valor = {p:.5f}\n')

if p < 0.05:
    print("Rejeita-se H0:\nHá evidências para concluir que há diferença significativa na idade dos pacientes com diagnóstico benigno e maligno.")
else:
    print("Não rejeita-se H0:\nNão há evidências suficientes para concluir que há diferença na idade dos pacientes com diagnóstico benigno e maligno.")

# Hypothesis 3
    # H0: There is no significant difference in mean tumor size between patients with and without a family history of breast cancer.
    # H1: There is a significant difference in mean tumor size between patients with and without a family history of breast cancer.

# Separando os tamanhos dos tumores por grupo de histórico familiar
tumor_semhistorico = df[df['History'] == 0]['Tumor Size (cm)']
tumor_comhistorico = df[df['History'] == 1]['Tumor Size (cm)']

# Aplicar o teste de Mann-Whitney
stat, p = mannwhitneyu(tumor_semhistorico, tumor_comhistorico, alternative='two-sided')

print(f'Teste de Mann-Whitney - Hipótese 3\n\nEstatística U = {stat:.4f}\np-valor = {p:.5f}\n')

if p < 0.05:
    print("Rejeita-se H0:\nHá evidências para concluir que há diferença significativa no tamanho médio dos tumores entre pacientes com ou sem histórico familiar de câncer de mama.")
else:
    print("Não rejeita-se H0:\nNão há evidências suficientes para concluir que há diferença significativa no tamanho médio dos tumores entre pacientes com ou sem histórico familiar de câncer de mama.")

# Hypothesis 4
    # H0: There is no significant association between a family history of breast cancer and diagnosis.
    # H1: There is a significant association between a family history of breast cancer and diagnosis.

# Tabela de contingência
contingency = pd.crosstab(df['History'], df['Diagnosis Result'])

# Aplicar teste do qui-quadrado
chi2, p, dof, expected = chi2_contingency(contingency)

print('Teste do Qui-Quadrado - Hipótese 4\n')
print(f'Estatística χ² = {chi2:.4f}\np-valor = {p:.5f}\n')

if p < 0.05:
    print("Rejeita-se H0:\nHá evidências de associação significativa entre histórico familiar e o diagnóstico.")
else:
    print("Não se rejeita H0:\nNão há evidências suficientes para afirmar que há associação significativa entre histórico familiar e o diagnóstico.")

# Hypothesis 5
    # H0: There is no significant association between menopausal status and diagnosis.
    # H1: There is a significant association between menopausal status and diagnosis.

# Tabela de contingência
contingency = pd.crosstab(df['Diagnosis Result'], df['Menopause'])

# Aplicar teste do qui-quadrado
chi2, p, dof, expected = chi2_contingency(contingency)

print('Teste do Qui-Quadrado - Hipótese 5\n')
print(f'Estatística χ² = {chi2:.4f}\np-valor = {p:.5f}\n')

if p < 0.05:
    print("Rejeita-se H0:\nHá evidências de associação significativa entre o status da menopausa e o diagnóstico.")
else:
    print("Não se rejeita H0:\nNão há evidências suficientes para afirmar que há associação significativa entre o status da menopausa e o diagnóstico.")
