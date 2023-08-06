import React from 'react';
import { Route, Routes } from 'react-router-dom';
import styles from './App.module.scss';
import { routes } from 'src/routes';
import { ProtectedRoute } from '../protected-route/ProtectedRoute';
import { LoginPage } from 'src/pages/LoginPage/LoginPage';
import { ProfilePage } from 'src/pages/ProfilePage/ProfilePage';
import { SignUpPage } from 'pages/SignUpPage/SignUpPage';
import { useDispatch, useSelector } from 'src/services/hooks';
import { authThunks, selectUserMe } from 'src/services/slices/authSlice';
import { KanbanPage } from 'pages/KanbanPage/KanbanPage';

export const App: React.FC = () => {
  const dispatch = useDispatch();
  const userMe = useSelector(selectUserMe);

  // Check if the user is logged in at the level of the app
  React.useEffect(() => {
    if (!userMe) dispatch(authThunks.userMe());
  }, [dispatch, userMe]);

  return (
    <Routes>
      {/* free access */}
      
      {/* <Route path={routes.home.path} element={<KanbanPage />} />
      <Route path={routes.canban.path} element={<KanbanPage />} /> */}

      <Route path={routes['sign-in'].path} element={<LoginPage />} />
      <Route path={routes['sign-up'].path} element={<SignUpPage />} />

      {/* protected */}
      <Route element={<ProtectedRoute />}>
        <Route path={routes['profile'].path} element={<ProfilePage />} />
        <Route path={routes['home'].path} element={<KanbanPage />} />
      </Route>

      {/* 404 */}
      <Route path={'*'} element={<div>Такой страницы не существует</div>} />
    </Routes>
  );
};
