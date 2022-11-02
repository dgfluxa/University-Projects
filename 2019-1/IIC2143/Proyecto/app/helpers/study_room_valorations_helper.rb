# frozen_string_literal: true

module StudyRoomValorationsHelper
  def calculate_availability(study_room)
    availability = 0.0
    if study_room.study_room_valorations != []
      study_room.study_room_valorations.each do |valoration|
        availability += valoration.availability
      end
      return (availability / study_room.study_room_valorations.size).round(2)
    else
      return '-'
    end
  end

  def calculate_noise(study_room)
    noise = 0.0
    if study_room.study_room_valorations != []
      study_room.study_room_valorations.each do |valoration|
        noise += valoration.noise
      end
      return (noise / study_room.study_room_valorations.size).round(2)
    else
      return '-'
    end
  end

  def calculate_plugs(study_room)
    plugs = 0.0
    if study_room.study_room_valorations != []
      study_room.study_room_valorations.each do |valoration|
        plugs += valoration.plugs
      end
      (plugs / study_room.study_room_valorations.size).round(2)
    else
      return '-'
    end
  end
end
