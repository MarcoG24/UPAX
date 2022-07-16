
function get_recommendations(){
    return new Promise((resolve, reject) => {
        const url = 'https://bffgtxi6gg.execute-api.us-east-2.amazonaws.com/prod/store/products/recommendations'
        $.get(url, function(response, status){
            if (status == 'success'){
                resolve(response.data);
            }
        })
    })
}

function get_products(){
    return new Promise((resolve, reject) => {
        const url = 'https://bffgtxi6gg.execute-api.us-east-2.amazonaws.com/prod/store/products'
        $.get(url, function(response, status){
            if (status == 'success'){
                resolve(response.data);
            }
        })
    })
}