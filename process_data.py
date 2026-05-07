import pandas as pd

# 1. Leer datos
df = pd.read_csv("data.csv")

# 2. Convertir fecha a tipo fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# 3. Crear columna total ventas
df["total_venta"] = df["cantidad"] * df["precio"]

# 4. Agrupar por producto
resumen_producto = df.groupby("producto")["total_venta"].sum().reset_index()

# 5. Agrupar por región
resumen_region = df.groupby("region")["total_venta"].sum().reset_index()

# 6. Guardar resultados en CSV
resumen_producto.to_csv("resumen_producto.csv", index=False)
resumen_region.to_csv("resumen_region.csv", index=False)

# 7. Mostrar resultados en consola
print("Resumen por producto:")
print(resumen_producto)

print("\nResumen por región:")
print(resumen_region)