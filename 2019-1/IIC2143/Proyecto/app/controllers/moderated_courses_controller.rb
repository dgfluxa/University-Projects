# frozen_string_literal: true

class ModeratedCoursesController < ApplicationController
  def update
    @course = Course.find(params[:course])
    @user = User.find(params[:user])
    moderated_course = ModeratedCourse.where(course: @course, user: @user)
    if moderated_course == []
      @moderated_course = ModeratedCourse.create(course: @course, user: @user)
      @moderated_course.user = @user
      @moderated_course.course = @course
      request = ModerationRequest.find_by(user: @user, course: @course)
      request.destroy
    else
      moderated_course.destroy_all
    end
    redirect_to '/requests'
  end
end
