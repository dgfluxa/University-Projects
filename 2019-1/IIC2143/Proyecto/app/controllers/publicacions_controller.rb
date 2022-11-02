# frozen_string_literal: true

class PublicacionsController < ApplicationController
  load_and_authorize_resource
  def index
    @publicaciones = Publicacion.all
  end

  def update
    @publicacion = Publicacion.find(params[:id])
    @course = @publicacion.course
    if @publicacion.update(publicacion_params)
      redirect_to course_publicacion_path(@course, @publicacion)
    else
      render :edit
    end
  end

  def show
    @course = Course.find(params[:course_id])
    @publicacion = Publicacion.find(params[:id])
    @favorite_publication_exists = FavoritePublication.where(publicacion: @publicacion, user: current_user) != []
  end

  def edit
    @publicacion = Publicacion.find(params[:id])
  end

  def create
    @publicacion = Publicacion.new(publicacion_params)
    @course = Course.find(params[:course_id])
    @publicacion.user = current_user
    @publicacion.puntaje = 0
    @publicacion.course = @course
    if @publicacion.save
      redirect_to course_path(@course)
    else
      redirect_to 'new'
    end
  end

  def new
    @publicacion = Publicacion.new
  end

  def destroy
    @publicacion = Publicacion.find(params[:id])
    @course = @publicacion.course
    @publicacion.destroy
    redirect_to course_path(@course)
  end

  private

  def publicacion_params
    params.require(:publicacion).permit(:titulo, :description, :contenido, :user, :course)
  end
end
