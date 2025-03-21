# Importar os dados do arquivo CSV
dados <- read.csv("dados_agricolas.csv")

# Exibir os dados importados
print("Dados importados:")
print(dados)

# Calcular estatísticas básicas
media_area <- mean(dados$Area..m2.)
desvio_area <- sd(dados$Area..m2.)

media_insumo <- mean(dados$Insumo..mL.)
desvio_insumo <- sd(dados$Insumo..mL.)

# Exibir os resultados
cat("\n=== Estatísticas das Áreas ===\n")
cat("Média das áreas (m²):", media_area, "\n")
cat("Desvio padrão das áreas (m²):", desvio_area, "\n")

cat("\n=== Estatísticas dos Insumos ===\n")
cat("Média dos insumos (mL):", media_insumo, "\n")
cat("Desvio padrão dos insumos (mL):", desvio_insumo, "\n")
