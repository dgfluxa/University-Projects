# frozen_string_literal: true

class StudentCoursesController < ApplicationController
  load_and_authorize_resource
  def update
    professor_course = ProfessorCourse.where(course: Course.find(params[:course]), user: current_user)
    student_course = StudentCourse.where(course: Course.find(params[:course]), user: current_user)
    if (student_course == []) && (professor_course == [])
      # Create student_course
      StudentCourse.create(course: Course.find(params[:course]), user: current_user)
      @student_course_exists = true
    elsif (student_course == []) && (professor_course != [])
      flash[:danger] = 'No puedes suscribirte como alumno en un curso en el que estas suscrito como profesor'
    else
      # Delete student_course
      student_course.destroy_all
      @student_course_exists = false
    end
    respond_to do |format|
      format.html {}
      format.js { render inline: 'location.reload();' }
    end
  end
end
