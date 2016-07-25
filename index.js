function ProductsViewModel() {
  var self = this;
  self.productsURI = 'http://localhost:3000/products';
  self.productidURI = 'http://localhost:3000/product';
  self.products = ko.observableArray();
  self.ajax = function(uri, method, data) {
    var request = {
        url: uri,
        type: method,
        contentType: "application/json",
        accepts: "application/json",
        dataType: 'json',
        data: JSON.stringify(data),
        error: function(jqXHR) {
            console.log("ajax error " + jqXHR.status);
        }
    };
  return $.ajax(request);
}
self.ajax(self.productsURI, 'GET').done(function(data) {
  for (var i = 0; i < data.length; i++) {
    // self.products.push({
    //     uri: ko.observable(data[i].ID),
    //     name: ko.observable(data[i].NAME),
    //     price: ko.observable(data[i].PRICE),
    //     done: ko.observable(data[i].done)
    // });
    self.ajax(self.productidURI + "/" + data[i].ID, 'GET').done(function(data) {
    for (var j = 0; j < data.length; j++) {
      self.products.push({
        uri: ko.observable(data[j].ID),
        name: ko.observable(data[j].NAME),
        price: ko.observable(data[j].PRICE),
        description: ko.observable(data[j].DESCRIPTION)
      });
    }
  });
  }
});
self.beginAdd = function() {
  $('#add').modal('show');
}
self.add = function(product) {
  self.ajax(self.productsURI, 'POST', product).done(function(data) {
    self.products.push({
      name: ko.observable(data.NAME),
      description: ko.observable(data.DESCRIPTION),
      price: ko.observable(data.PRICE),
      done: ko.observable(data.done)
    });
  });
}
self.beginEdit = function(product) {
  editProductViewModel.setProduct(product);
  $('#edit').modal('show');
}
self.edit = function(product, data) {
  self.ajax(product.uri(), 'PUT', data).done(function(res) {
      self.updateProduct(product, res.product);
  });
}
self.updateProduct = function(product, newProduct) {
  var i = self.products.indexOf(product);
  self.products()[i].uri(newProduct.uri);
  self.products()[i].name(newProduct.name);
  self.products()[i].price(newProduct.price);
  self.products()[i].description(newProduct.description);
  self.products()[i].done(newProduct.done);
}
self.remove = function(product) {
  self.ajax(self.productsURI, 'DELETE').done(function() {
    self.products.remove(product);
  });
}
}
function AddProductViewModel() {
var self = this;
self.name = ko.observable();
self.description = ko.observable();
self.price = ko.observable();

self.addProduct = function() {
  $('#add').modal('hide');
  productsViewModel.add({
    name: self.name(),
    description: self.description(),
    price: self.price(),
  });
  self.name("");
  self.description("");
  self.price("");
}
}

function EditProductViewModel() {
var self = this;
self.NAME = ko.observable();
self.DESCRIPTION = ko.observable();
self.PRICE = ko.observable();
self.done = ko.observable();

self.setProduct = function(product) {
  self.product = product;
  self.name(product.NAME());
  self.price(product.PRICE());
  self.description(product.DESCRIPTION());
  self.done(product.done());
  $('edit').modal('show');
}
self.editProduct = function() {
  $('#edit').modal('hide');
  productsViewModel.edit(self.product, {
      name: self.NAME(),
      description: self.DESCRIPTION(),
      price: self.PRICE(),
      done: self.done()
  });
}
}

var productsViewModel = new ProductsViewModel();
var addProductViewModel = new AddProductViewModel();
var editProductViewModel = new EditProductViewModel();
ko.applyBindings(productsViewModel, $('#main')[0]);
ko.applyBindings(addProductViewModel, $('#add')[0]);
ko.applyBindings(editProductViewModel, $('#edit')[0]);
