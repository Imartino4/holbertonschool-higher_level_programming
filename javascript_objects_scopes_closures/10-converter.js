#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
/* Primera vez que se llama a la funcion se guarda la base
y la segunda vez se aplica la conversion al numero */
