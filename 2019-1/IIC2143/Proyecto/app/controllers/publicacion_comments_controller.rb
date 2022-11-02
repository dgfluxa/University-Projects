# frozen_string_literal: true

class PublicacionCommentsController < ApplicationController
  load_and_authorize_resource
  before_action :publicacion_comment_params, only: %i[create update]
  before_action :set_publicacion, only: %i[create update destroy edit]
  before_action :set_user, only: [:create]
  def new
    @publicacion_comment = PublicacionComment.new
  end

  def create
    @publicacion_comment = PublicacionComment.new(publicacion_comment_params)
    @publicacion_comment.user_id = @user.id
    @publicacion_comment.publicacion_id = @publicacion.id
    if @publicacion_comment.save
      redirect_to course_publicacion_path(@course, @publicacion)
    else
      render :new
    end
  end

  def edit
    @publicacion_comment = PublicacionComment.find(params[:id])
  end

  def update
    @publicacion_comment = PublicacionComment.find(params[:id])
    if @publicacion_comment.update(publicacion_comment_params)
      redirect_to course_publicacion_path(@course, @publicacion)
    else
      render :edit
    end
  end

  def index
    @publicacion_comment = PublicacionComment.all
  end

  def show
    @publicacion_comment = PublicacionComment.find(params[:id])
  end

  def destroy
    @publicacion_comment = PublicacionComment.find(params[:id])
    @publicacion_comment.destroy
    redirect_to course_publicacion_path(@course, @publicacion)
  end
end

private
def publicacion_comment_params
  params.require(:publicacion_comment).permit(:body)
end

def set_publicacion
  @publicacion = Publicacion.find(params[:publicacion_id])
  @course = Course.find(params[:course_id])
end

def set_user
  @user = current_user
  @course = Course.find(params[:course_id])
end
