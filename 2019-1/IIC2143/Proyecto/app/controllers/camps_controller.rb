# frozen_string_literal: true

class CampsController < ApplicationController
  load_and_authorize_resource
  def show
    @camps = Camp.find(params[:id])
  end

  def index
    @camps = Camp.all
  end

  def new
    @camps = Camp.new
  end

  def edit
    @camps = Camp.find(params[:id])
  end

  def create
    @camps = Camp.new(camp_params)
    if @camps.save
      redirect_to @camps
    else
      render :new
    end
  end

  def update
    @camps = Camp.find(params[:id])
    if @camps.update(camp_params)
      redirect_to @camps
    else
      render 'edit'
    end
  end

  def destroy
    @camps = Camp.find(params[:id])
    @camps.destroy
    redirect_to camps_path
  end

  private

  def camp_params
    params.require(:camp).permit(:nombre, :ubicacion, :url)
  end
end
