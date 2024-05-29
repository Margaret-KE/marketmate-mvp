module.exports = {
  transform: {
    '^.+\\.jsx?$': 'babel-jest',
  },
  transformIgnorePatterns: [
    'node_modules/(?!react|react-dom)' // Adjust if you need to transform other node_modules
  ],
};

