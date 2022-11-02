# frozen_string_literal: true

class StudyGroupsController < ApplicationController
  load_and_authorize_resource
  def new
    @user = current_user
    @study_room = StudyRoom.find(params[:room_id])
    @course = Course.find(params[:course_id])
    @study_group = StudyGroup.new
  end

  def create
    @user = current_user
    @study_group = StudyGroup.new(study_group_params)
    @study_room = StudyRoom.find(params[:room_id])
    @course = Course.find(params[:course_id])
    @study_group.course = @course
    @study_group.study_room = @study_room
    @study_group.user = current_user
    if @study_group.save
      SubscribedUser.create(study_group: @study_group, user: @user)
      redirect_to study_groups_path
    else
      render 'new'
    end
  end

  def edit; end

  def update
    @study_group = StudyGroup.find(params[:id])
    if @study_group.update(study_group_params)
      redirect_to @study_group
    else
      render :edit
    end
  end

  def show
    @study_group = StudyGroup.find(params[:id])
    @subscribed_user_exists = SubscribedUser.where(study_group: @study_group, user: current_user) != []
  end

  def index
    @study_groups = StudyGroup.all
  end

  def destroy
    @study_group = StudyGroup.find(params[:id])
    @study_group.destroy
    redirect_to study_groups_path
  end

  private

  def study_group_params
    params.permit(:course, :study_room, :max, :duration)
  end
end
