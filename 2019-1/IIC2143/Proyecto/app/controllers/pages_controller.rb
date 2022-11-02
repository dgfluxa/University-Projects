# frozen_string_literal: true

class PagesController < ApplicationController
  def home; end

  def profile
    @user = User.find(params[:id])
    @conversacion = Conversation.new
  end

  def paso
    @courses = Course.all
  end

  def paso2
    @study_rooms = StudyRoom.all
    @course = Course.find(params[:id])
  end

  def busqueda
    @palabra = params[:buscoclase]['course']
    @clases_ofrecidas = Ofertclase.all
  end

  def busqueda2
    @palabra = params[:buscoclase]['course']
    @clases_buscadas = Buscoclase.all
    @study_groups = StudyGroup.all
  end

  def busqueda_grupos
    @palabra = params[:buscoclase]['course']
    @study_groups = StudyGroup.all
  end

  def busqueda_publicacion
    @palabra = params[:buscoclase]['course']
    @course = Course.find(params[:id])
    @publicaciones = @course.publicacions
  end

  def moderators
    @users = User.all
  end

  def make_admin
    @user = User.find(params[:user_id])
    @user.update(admin: true)
    redirect_to moderators_path
  end

  def administrators
    @users = User.all
  end

  def delete_user
    @user = User.find(params[:user_id])
    @user.destroy
  end

  def busqueda_cursos
    @palabra = params[:buscoclase]['course']
    @courses = Course.all
  end
end
