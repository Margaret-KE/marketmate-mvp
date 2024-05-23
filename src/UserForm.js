// UserForm.js
import React from 'react';

const UserForm = () => (
  <form>
    <label htmlFor="username">Username</label>
    <input id="username" name="username" type="text" />
    <label htmlFor="email">Email</label>
    <input id="email" name="email" type="email" />
    <label htmlFor="password">Password</label>
    <input id="password" name="password" type="password" />
  </form>
);

export default UserForm;

