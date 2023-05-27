$(document).ready(function() {
            
    $('input[type=radio][name=status]').change(function() {
        var category = $(this).val();
        filterProducts(category);
    });

    function filterProducts(category) {
    $.ajax({
        url: '/ajax-load/',
        data: {
            category: category
        },
        success: function(data) {
            var productsContainer = $('#ajax_id');
            productsContainer.empty();
            var products = data.products;
            
            if (products.length === 0) {
                var productHtml = `<h1 style="color:red;">No product is found</h1>`
                productsContainer.append(productHtml);
            } else {
                for (var i = 0; i < products.length; i++) {
                    var product = products[i];
                    var productHtml = 
                    `<div class="p-item">                            
                        <div class="p-item-inner">
                            <div class="p-item-img"><a
                                    href="#"><img
                                        src="media/${product.image}"
                                        alt="${product.product_name}"
                                        width="500" height="600"></a></div>
                            <div class="p-item-details">
                                <h4 class="p-item-name"> <a
                                        href="#">${product.product_name}</a></h4>
                                <div class="p-item-price">
                                    <span>${product.price}৳</span>
                                </div>
                                <div class="actions">
                                    <span class="st-btn btn-add-cart" type="button"><i
                                            class="material-icons">shopping_cart</i> Buy Now</span>
                                    <span class="st-btn btn-compare"><i
                                            class="material-icons">library_add</i>Add to Compare</span>
                                </div>
                            </div>
                        </div>                                
                    </div>`;
                    productsContainer.append(productHtml);
                }
            }
        }
    });
}            
});