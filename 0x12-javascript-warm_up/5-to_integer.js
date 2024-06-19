#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
