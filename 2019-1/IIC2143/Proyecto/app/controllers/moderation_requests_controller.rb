# frozen_string_literal: true

class ModerationRequestsController < ApplicationController
  before_action :set_course, only: %i[update edit create destroy update]
  def new
    @moderation_request = ModerationRequest.new
  end

  def edit
    @moderation_request = ModerationRequest.find(params[:id])
  end

  def update
    @moderation_request = ModerationRequest.find(params[:id])
    if @moderation_request.update(moderation_request_params)
      @moderation_request.user = current_user
      @moderation_request.course = @course
      redirect_to course_path(@course)
    else
      render :edit
    end
  end

  def show
    @moderation_request = ModerationRequest.find(params[:id])
  end

  def create
    moderation_requests = ModerationRequest.where(course: @course, user: current_user)
    if moderation_requests == []
      @moderation_request = ModerationRequest.new(moderation_request_params)
      @moderation_request.user = current_user
      @moderation_request.course = @course
    else
      moderation_requests.destroy_all
      @moderation_request = ModerationRequest.new(moderation_request_params)
      @moderation_request.user = current_user
      @moderation_request.course = @course
    end
    if @moderation_request.save
      redirect_to course_path(@course)
    else
      redirect_to :new
    end
  end

  def destroy
    @moderation_request = ModerationRequest.find(params[:id])
    @moderation_request.destroy
    redirect_to '/requests'
  end
end
private
def moderation_request_params
  params.require(:moderation_request).permit(:description, :photo)
end

def set_course
  @course = Course.find(params[:course_id])
end
