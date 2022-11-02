# frozen_string_literal: true

class OccupiedRoomsController < ApplicationController
  load_and_authorize_resource
  before_action :set_study_room, only: %i[new update create destroy show]
  before_action :set_user, only: %i[new update create destroy show]

  def new
    @occupied_room = OccupiedRoom.new
  end

  def create
    @occupied_room = OccupiedRoom.new(occupied_room_params)
    @occupied_room.study_room = @study_room
    @occupied_room.user = current_user
    # Se podria agregar que se borren los grupos de estudios en el periodo de tiempo ingresado
    if @occupied_room.save
      redirect_to @study_room
    else
      redirect_to @study_room
    end
  end

  def edit
    @occupied_room = OccupiedRoom.find(params[:id])
  end

  def update
    @occupied_room = OccupiedRoom.find(params[:id])
    if @occupied_room.update(occupied_room_params)
      redirect_to @study_room
    else
      render :edit
    end
  end

  def destroy
    @occupied_room = OccupiedRoom.find(params[:id])
    @occupied_room.destroy
    redirect_to @study_room
  end

  private

  def occupied_room_params
    params.require(:occupied_room).permit(:study_room, :from, :to)
  end

  def set_study_room
    @study_room = StudyRoom.find(params[:study_room_id])
  end

  def set_user
    @user = current_user
  end
end
