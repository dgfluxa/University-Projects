# frozen_string_literal: true

class LikeComentsController < ApplicationController
  def destroy
    @publicacion = Publicacion.find(params[:publicacion_id])
    @comment = PublicacionComment.find(params[:publicacion_comment_id])
    if !already_liked?
      @like = LikeComent.new
      @like.publicacion_comment_id = @comment.id
      @like.user = current_user
      @like.like = 0
      @like.save
    else
      @like = LikeComent.find_by(user: current_user, publicacion_comment: params[:publicacion_comment_id])
      @like.like = 0
    end
    @like.save!
    redirect_to course_publicacion_path(@publicacion.course, @publicacion)
  end

  def create
    @publicacion = Publicacion.find(params[:publicacion_id])
    @comment = PublicacionComment.find(params[:publicacion_comment_id])
    if already_liked?
      @like_coments = LikeComent.find_by(user: current_user, publicacion_comment: params[:publicacion_comment_id])
      @like_coments.like = 1
    else
      @like_coments = LikeComent.new
      @like_coments.publicacion_comment_id = @comment.id
      @like_coments.user = current_user
      @like_coments.like = 1
    end
    @like_coments.save
    redirect_to course_publicacion_path(@publicacion.course, @publicacion)
  end

  private

  def already_liked?
    LikeComent.where(user_id: current_user, publicacion_comment: params[:publicacion_comment_id]).exists?
  end
end
