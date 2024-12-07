function startGame() {
  alert("Game starting! Prepare to play.");
}

// Example of a dynamic leaderboard
const leaderboard = [
  { name: "Player1", score: 100 },
  { name: "Player2", score: 90 },
  { name: "Player3", score: 80 },
];

const leaderboardList = document.getElementById("leaderboard-list");
leaderboard.forEach(player => {
  const listItem = document.createElement("li");
  listItem.textContent = `${player.name}: ${player.score}`;
  leaderboardList.appendChild(listItem);
});
