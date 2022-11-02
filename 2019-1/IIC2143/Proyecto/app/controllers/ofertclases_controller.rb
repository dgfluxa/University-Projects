# frozen_string_literal: true

class OfertclasesController < ApplicationController
  def index
    @ofertclases = Ofertclase.new
    @clases_ofrecidas = Ofertclase.all
    @courses = Course.all
    @rooms = StudyRoom.all
    @user = current_user
  end

  def new
    @ofertclases = Ofertclase.new
    @courses = Course.all
    @rooms = StudyRoom.all
  end

  def create
    @ofertclases = Ofertclase.new(ofert_clases_params)
    @ofertclases.user = current_user.email
    if @ofertclases.save
      redirect_to clases_particulares_path
    else
      redirect_to clases_particulares_path
    end
  end

  def destroy
    @ofertclases = Ofertclase.find(params[:id])
    @ofertclases.destroy
    redirect_to clases_particulares_path
  end

  def edit
    @ofertclases = Ofertclase.find(params[:id])
    @courses = Course.all
    @rooms = StudyRoom.all
  end

  def update
    @ofertclases = Ofertclase.find(params[:id])
    @ofertclases.user = current_user.email
    if @ofertclases.update(ofert_clases_params)
      redirect_to clases_particulares_path
    else
      render 'edit'
    end
  end

  def show
    @course = Course.all
    @ofertclases = Ofertclase.find(params[:id])
  end

  private

  def ofert_clases_params
    params.require(:ofertclase).permit(:precio, :course, :sala, :description, :time)
  end
end
