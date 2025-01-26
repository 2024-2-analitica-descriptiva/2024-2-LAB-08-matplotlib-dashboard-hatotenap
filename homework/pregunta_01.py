# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    # Crear la carpeta docs si no existe
    
    os.makedirs("docs", exist_ok=True)


    df= pd.read_csv("files/input/shipping-data.csv")

    # vamos a crear la función para crear la grafica de los envíos por bodega
    def create_visual_for_shipping_per_warehouse(df):
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel=" Record Count",
            color="tab:blue",
            fontsize=8,
            )
        #bordes que no se vean 
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        #guardamos la imagen 
        plt.savefig("docs/shipping_per_warehouse.png")
        plt.close()

    def create_visual_for_mode_of_shipment(df):
        df = df.copy()
        plt.figure()
        counts=df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of shipment",
            # Hueco del pie que es del 35% de la imagen
            wedgeprops= dict(width =0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.savefig("docs/mode_of_shipment.png")
        plt.close()

    def create_visual_for_average_customer_rating(df):
        df=df.copy()
        plt.figure()
        df=(
            df[["Mode_of_Shipment","Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df=df[["mean","min", "max"]]
        #se construye un agrafica horizontal 
        plt.barh(
            y=df.index.values, 
            width=df["max"].values -1,
            left=df["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors=[
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]
        plt.barh(
            y=df.index.values, 
            width=df["mean"].values -1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/average_customer_rating.png")
        plt.close()
    

    def create_visual_for_weight_distribution(df):
        df = df.copy()
        plt.figure()

        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/weight_distribution.png")
        plt.close()

    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    # Archivo HTML
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shipping Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: auto;
                text-align: center;
            }
            img {
                max-width: 100%;
                height: auto;
                margin-bottom: 20px;
            }
            h1 {
                margin-top: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Shipping Dashboard</h1>
            <h2>Shipping per Warehouse</h2>
            <img src="docs/shipping_per_warehouse.png" alt="Shipping per Warehouse">
            <h2>Mode of Shipment</h2>
            <img src="docs/mode_of_shipment.png" alt="Mode of Shipment">
            <h2>Average Customer Rating</h2>
            <img src="docs/average_customer_rating.png" alt="Average Customer Rating">
            <h2>Weight Distribution</h2>
            <img src="docs/weight_distribution.png" alt="Weight Distribution">
        </div>
    </body>
    </html>
    """

    # Guardar el archivo HTML
    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    





   







