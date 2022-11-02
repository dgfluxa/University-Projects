# frozen_string_literal: true

class ProfessorCoursesController < ApplicationController
  load_and_authorize_resource
  def update
    professor_course = ProfessorCourse.where(course: Course.find(params[:course]), user: current_user)
    student_course = StudentCourse.where(course: Course.find(params[:course]), user: current_user)
    if (professor_course == []) && (student_course == [])
      # Create professor_course
      ProfessorCourse.create(course: Course.find(params[:course]), user: current_user)
      @professor_course_exists = true
    elsif (professor_course == []) && (student_course != [])
      flash[:danger] = 'No puedes suscribirte como profesor a un curso en el que estas suscrito como alumno'

    else
      # Delete professor_course
      professor_course.destroy_all
      @professor_course_exists = false
    end
    respond_to do |format|
      format.html {}
      format.js { render inline: 'location.reload();' }
    end
  end
end
