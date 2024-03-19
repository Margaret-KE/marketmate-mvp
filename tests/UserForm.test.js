import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import UserForm from './UserForm';

describe('UserForm', () => {
  it('renders a form with input fields', () => {
    const { getByLabelText } = render(<UserForm />);
    expect(getByLabelText('Username')).toBeInTheDocument();
    expect(getByLabelText('Email')).toBeInTheDocument();
    expect(getByLabelText('Password')).toBeInTheDocument();
  });

  it('submits the form with user input', () => {
    const handleSubmit = jest.fn();
    const { getByLabelText, getByText } = render(<UserForm onSubmit={handleSubmit} />);
    fireEvent.change(getByLabelText('Username'), { target: { value: 'testuser' } });
    fireEvent.change(getByLabelText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(getByLabelText('Password'), { target: { value: 'password123' } });
    fireEvent.click(getByText('Submit'));
    expect(handleSubmit).toHaveBeenCalledWith({
      username: 'testuser',
      email: 'test@example.com',
      password: 'password123',
    });
  });
});

