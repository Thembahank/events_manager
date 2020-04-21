import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
   theme: {
    themes: {
      light: {
        primary: '#2368a2',
        secondary: '#424242',
        accent: '#6ed7d3',
        error: '#FF5252',
        info: '#2196F3',
        success: '#74d99f',
        warning: '#f4ca64',
        dark:'#212429',
        grey:'#f5f7fa',
      }
    },
  },
});
