import React from 'react';
import clsx from 'clsx';
import style from './Projects.module.scss';
import { NavLink } from 'react-router-dom';
import { ReactComponent as ProjectIcon } from 'assets/project-icon.svg';
import {
  selectCurrentProject,
  selectProjectInfo,
  setCurrent,
} from 'src/services/slices/projectSlice';
import { useDispatch, useSelector } from 'src/services/hooks';
import { HeaderState, setHeaderState } from 'src/services/slices/headerSlice';

export const Projects = (): JSX.Element => {
  const projectsArr = useSelector(selectProjectInfo);
  const currentProject = useSelector(selectCurrentProject);
  const dispatch = useDispatch();

  const handleClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    const arr = e.currentTarget.id.split('-');
    const id = arr[0];
    dispatch(setCurrent(Number(id)));
    dispatch(setHeaderState(HeaderState.KANBAN));
  };

  function renderProjects(): React.ReactNode[] {
    return projectsArr.map((project) => {
      return (
        <li key={project.id}>
          <NavLink
            to={`/${project.id}`}
            className={clsx(style.projects__nav, {
              [style.projects__nav_active]: currentProject.id === project.id,
            })}
            onClick={(e) => handleClick(e)}
            id={`${project.id}-project`}
          >
            <ProjectIcon className={style.projects__icon} />
            <span className={style.projects__name}>{project.name}</span>
          </NavLink>
        </li>
      );
    });
  }

  return (
    <section className={style.projects}>
      <h3 className={style.projects__title}>Проекты</h3>
      <button className={style.projects__filter}></button>
      <ul className={style.projects__list}>{renderProjects()}</ul>
    </section>
  );
};