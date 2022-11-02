# frozen_string_literal: true

class StudyRoomsController < ApplicationController
  load_and_authorize_resource
  before_action :set_camp, only: %i[new update edit create destroy]

  def index
    @study_rooms = StudyRoom.all
  end

  def show
    @study_rooms = StudyRoom.find(params[:id])
  end

  def new
    @study_rooms = StudyRoom.new
  end

  def create
    @study_rooms = StudyRoom.new(study_room_params)
    @study_rooms.camp_id = @camps.id
    if @study_rooms.save
      redirect_to camp_path(@camps.id)
    else
      render :new
    end
  end

  def edit
    @study_rooms = StudyRoom.find(params[:id])
    @study_rooms.camp_id = @camps.id
  end

  def update
    @study_rooms = StudyRoom.find(params[:id])
    if @study_rooms.update(study_room_params)
      redirect_to study_rooms_path
    else
      render 'edit'
    end
  end

  def destroy
    @study_rooms = StudyRoom.find(params[:id])
    @study_rooms.destroy
    redirect_to study_rooms_path
  end
end

private
def study_room_params
  params.require(:study_room).permit(:name, :ubication, :availability_score, :noise_score, :plug_score, :camp_id)
end

def set_camp
  @camps = Camp.find(params[:camp_id])
end
