//require our dependencies
//Run ./node_modules/.bin/webpack --config webpack.config.js

const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

module.exports = {
    //the base directory (absolute path) for resolving the entry option
    context: __dirname,
    //the entry point we created earlier. Note that './' means
    //your current directory. You don't have to specify the extension  now,
    //because you will specify extensions later in the `resolve` section
    entry: [
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        './static/js/main',
    ],

    output: {
        //where you want your compiled bundle to be stored
        path: path.resolve('./static/bundles/'),
        //naming convention webpack should use for your files
        filename: '[name]-[hash].js',
        publicPath: 'http://localhost:3000/assets/bundles/',
    },
    externals: 'Axios',
    plugins: [
        //tells webpack where to store data about your bundles.
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    
    module: {
        loaders: [
            //a regexp that tells webpack use the following loaders on all 
            //.js and .jsx files
            {
                test: /\.jsx?$/,
                //we definitely don't want babel to transpile all the files in 
                //node_modules. That would take a long time.
                exclude: /node_modules/, 
                //use the babel loader 
                loader: 'react-hot-loader/webpack'
            },
            {
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    //specify that we will be dealing with React code
                    presets: ['react']
                }
            }
          ]
    },
    
    resolve: {
        //tells webpack where to look for modules
        moduleExtensions: ['node_modules'],
        //extensions that should be used to resolve modules
        extensions: ['.js', '.jsx']
    }   
};