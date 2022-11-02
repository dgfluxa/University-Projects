# frozen_string_literal: true

class OccupiedRoom < ApplicationRecord
  belongs_to :study_room
  belongs_to :user
end
