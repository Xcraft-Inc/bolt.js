'use strict';

const binary = require ('node-pre-gyp');
const path = require ('path');
const binding_path = binary.find (
  path.resolve (path.join (__dirname, './package.json'))
);
const bolt = require (binding_path);

bolt.Open ();
