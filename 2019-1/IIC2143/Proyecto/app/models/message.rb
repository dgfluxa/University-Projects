# frozen_string_literal: true

class Message < ApplicationRecord
  belongs_to :conversation
  validates :texto, presence: true
end
