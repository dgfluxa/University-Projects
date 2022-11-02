# frozen_string_literal: true

class CoursesController < ApplicationController
  load_and_authorize_resource
  def new
    @course = Course.new
  end

  def create
    @course = Course.new(course_params)
    if @course.save
      redirect_to courses_path
    else
      render 'new'
    end
  end

  def edit
    @course = Course.find(params[:id])
  end

  def update
    @course = Course.find(params[:id])
    if @course.update(course_params)
      redirect_to courses_path
    else
      render :edit
    end
  end

  def show
    @course = Course.find(params[:id])
    @student_course_exists = StudentCourse.where(course: @course, user: current_user) != []
    @professor_course_exists = ProfessorCourse.where(course: @course, user: current_user) != []
    @publicaciones = Publicacion.all
  end

  def index
    @courses = Course.all
  end

  def destroy
    @course = Course.find(params[:id])
    @course.destroy
    redirect_to courses_path
  end

  private

  def course_params
    params.require(:course).permit(:name, :sigla, :description)
  end

  def set_course
    @course = Course.find(params[:id])
  end
end
