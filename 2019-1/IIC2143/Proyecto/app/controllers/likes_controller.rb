# frozen_string_literal: true

class LikesController < ApplicationController
  def destroy
    @publicacion = Publicacion.find(params[:publicacion_id])
    @course = Course.find(params[:course_id])
    if !already_liked?
      @like = Like.new
      @like.publicacion = @publicacion
      @like.user = current_user
      @like.like = 0
    else
      @like = Like.find_by(user: current_user, publicacion: @publicacion)
      @like.like = 0
    end
    @like.save
    redirect_to course_publicacion_path(@course, @publicacion)
  end

  def create
    @course = Course.find(params[:course_id])
    @publicacion = Publicacion.find(params[:publicacion_id])
    if already_liked?
      @like = Like.find_by(user: current_user, publicacion: @publicacion)
      @like.like = 1
    else
      @like = Like.new
      @like.publicacion = @publicacion
      @like.user = current_user
      @like.like = 1
    end
    @like.save
    redirect_to course_publicacion_path(@course, @publicacion)
  end

  private

  def already_liked?
    Like.where(user_id: current_user, publicacion: Publicacion.find(params[:publicacion_id])).exists?
  end
end
