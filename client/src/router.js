import VueRouter from 'vue-router'
import Home from './pages/Home'
import Profile from './pages/Profile'
import Register from './pages/Register'
import ListItems from './pages/ListItems'
import ItemDetails from './pages/ItemDetails'
import EditItem from './pages/EditItem'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/profile', component: Profile, name: 'Profile' },
  { path: '/register', component: Register, name: 'Register' },
  { path: '/listings', component: ListItems, name: 'ListItems' },
  { path: '/listings/:item_id', component: ItemDetails, name: 'ItemDetails' },
  { path: '/edit/:item_id', component: EditItem, name: 'EditItem' }
]

export default new VueRouter({ routes, mode: 'history' })
