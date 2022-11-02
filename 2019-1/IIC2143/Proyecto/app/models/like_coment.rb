# frozen_string_literal: true

class LikeComent < ApplicationRecord
  belongs_to :user
  belongs_to :publicacion_comment
end
