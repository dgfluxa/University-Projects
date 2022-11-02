# frozen_string_literal: true

class StudyRoomCommentsController < ApplicationController
  load_and_authorize_resource
  before_action :study_room_comment_params, only: %i[create update]
  before_action :set_study_room, only: %i[new update create destroy show]
  before_action :set_user, only: %i[new update create destroy show]

  def index
    @study_room_comment = StudyRoom.all
  end

  def show
    @study_room_comment = StudyRoomComment.find(params[:id])
  end

  def new
    @study_room_comment = StudyRoomComment.new
  end

  def edit
    @study_room_comment = StudyRoomComment.find(params[:id])
  end

  def create
    @study_room_comment = StudyRoomComment.new(study_room_comment_params)
    @study_room_comment.study_room_id = @study_room.id
    @study_room_comment.user_id = @user.id
    if @study_room_comment.save
      redirect_to @study_room
    else
      render :new
    end
  end

  def destroy
    @study_room_comment = StudyRoomComment.find(params[:id])
    @study_room_comment.destroy
    redirect_to @study_room
  end

  def update
    @study_room_comment = StudyRoomComment.find(params[:id])
    if @study_room_comment.update(study_room_comment_params)
      redirect_to @study_room
    else
      render 'edit'
    end
  end
end

private
def study_room_comment_params
  params.require(:study_room_comment).permit(:user_id, :body, :study_room_id)
end

def set_study_room
  @study_room = StudyRoom.find(params[:study_room_id])
end

def set_user
  @user = current_user
end
