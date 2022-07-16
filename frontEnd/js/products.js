var data_products;
$(document).ready(function(){
    
    var productsTable = document.getElementById("products-table");
    retrieve_products().then(products_recomendated  => {
        if (products_recomendated) {
            let products = 0;
            let number_row = 1;
            let row;
            data_products = products_recomendated;
            console.log(products_recomendated.length)
            products_recomendated.forEach(product => {
                if (number_row === 1) {
                    card = create_card(product)
                    col = create_col();
                    col.append(card);
                    row = create_row(row);
                    row.append(col);
                    number_row = number_row + 1;
                    products = products + 1;
                    if (products_recomendated.length === products) {
                        productsTable.append(row);
                    }
                } else {
                    card = create_card(product)
                    col = create_col();
                    col.append(card);
                    row.append(col);
                    productsTable.append(row);
                    row = "";
                    number_row = 1;
                    products = products + 1;
                }
                console.log(product)
                ;
            });
        }
      });
});

async function retrieve_recommendations(){
    const data_recommendations = await get_recommendations();
    return data_recommendations
}

async function retrieve_products(){
    const data_recommendations = await get_products();
    return data_recommendations
}

function onClick(product){
    console.log(product);
    data_products.forEach(element => {
        if (element[0] === product) {
            console.log(element)
        }
    });
}

function create_col(){
    var col = document.createElement("div");
    col.className = "col";
    return col;
}

function create_row(row_id){
    var row = document.createElement("div");
    row.className = "row align-items-center";
    row.id = row_id;
    return row;
}

function create_card(product){
    var card = document.createElement("div");
    card.className ="card mb-3";
    card.style.maxWidth = '640px'
    card.id = "card" + product[0];
    
    var row1 = document.createElement("div");
    row1.className = 'row g-0';

    var col1 = document.createElement("div");
    col1.className = "col-md-4";

    var image_card = document.createElement("img");
    image_card.src = product[2];
    image_card.className = "img-fluid rounded-start"

    col1.append(image_card);
    row1.append(col1)

    var col2 = document.createElement("div");
    col2.className = "col-md-8";

    var card_body = document.createElement("div");
    card_body.className = "card-body";

    var card_title = document.createElement("h5");
    card_title.className = "card-title";
    card_title.innerHTML = product[1];

    var p1 = document.createElement("p");
    p1.className = "card-text";
    p1.innerHTML = product[3];

    var small = document.createElement("small");
    small.className = "text-muted"
    small.innerHTML = "$" + product[4] + " (" + product[5] + " units available)"

    var p_small = document.createElement("p");
    p_small.className = "card-text";

    var button_div = document.createElement("div");
    button_div.className = "text-end";

    var a = document.createElement("a");
    a.href = "javascript:onClick("+product[0]+");";
    a.className = "btn btn-primary";
    a.innerHTML = "Add";

    button_div.append(a);

    p_small.append(small);
    card_body.append(card_title);
    card_body.append(p1);
    card_body.append(p_small);
    card_body.append(button_div);

    col2.append(card_body);
    row1.append(col2);

    card.append(row1);
    return card
}